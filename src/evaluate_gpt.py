import argparse
import math
from openai import AsyncOpenAI, AsyncAzureOpenAI, APITimeoutError, APIConnectionError, RateLimitError, InternalServerError
import os
from tqdm import tqdm
import pathlib
import traceback
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type,
    before_sleep_log
)
import asyncio, dataclasses
from dotenv import load_dotenv
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.WARN)
logger = logging.getLogger(__name__)

from utils import read_json, write_json, generate_unique_id, batched

CHAT_COMPLETION_MODELS = ["gpt-3.5-turbo", "gpt-4"]
TEXT_COMPLETION_MODELS = ["text-davinci-003"]
API_MODELS = CHAT_COMPLETION_MODELS + TEXT_COMPLETION_MODELS

@dataclasses.dataclass
class ModelResponse:
    text: str
    usage: dict

@retry(retry=retry_if_exception_type((APITimeoutError, APIConnectionError, RateLimitError, InternalServerError)), wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10), before_sleep=before_sleep_log(logger, logging.DEBUG))
async def chat_completion(client, messages, model="gpt-3.5-turbo", model_args=None):
    if model_args is None:
        model_args = {}
    
    response = await client.chat.completions.create(model=model, messages=messages, **model_args)
    text = response.choices[0].message.content.strip()
    usage = response.usage
    
    return ModelResponse(text, dict(usage))

@retry(retry=retry_if_exception_type((APITimeoutError, APIConnectionError, RateLimitError, InternalServerError)), wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10), before_sleep=before_sleep_log(logger, logging.DEBUG))
async def text_completion(client, prompt, model="text-davinci-003", model_args=None):
    if model_args is None:
        model_args = {}
    
    response = client.completions.create(model=model, prompt=prompt, **model_args)
    text = response.choices[0].text.strip()
    usage = response.usage

    return ModelResponse(text, dict(usage))

@torch.no_grad()
def compute_perplexity(text, model, tokenizer, device="cuda"):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    input_logprobs = []
    logits = model(input_ids.to(device)).logits
    all_logprobs = torch.log_softmax(logits.double(), dim=2)

    for k in range(input_ids.shape[1]):
        input_logprobs.append(all_logprobs[0, k-1, input_ids[0, k]].cpu())

    perplexity = 2 ** -torch.mean(torch.tensor(input_logprobs))

    return perplexity.item()

def load_model(model_path="gpt2", tokenizer_path="gpt2", model_args=None, cache_dir=None, device="cuda"):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, cache_dir=cache_dir)
    model = AutoModelForCausalLM.from_pretrained(model_path, cache_dir=cache_dir).to(device)
    model.eval()
    return model, tokenizer

def evaluate_lm(prompt, model, tokenizer, model_args=None, device="cuda"):
    perplexity = compute_perplexity(prompt, model, tokenizer, device=device)
    return perplexity

async def batch_chat_completion(client, batch, model, model_args):
    tasks = []
    
    for sample in batch:
        tasks.append(asyncio.create_task(chat_completion(client, [{"role": "user", "content": sample["prompt"].strip()}], model=model, model_args=model_args)))
    
    results = await asyncio.gather(*tasks)

    return results

async def batch_text_completion(client, batch, model, model_args):
    tasks = []
    
    for sample in batch:
        tasks.append(asyncio.create_task(text_completion(client, sample["prompt"].strip(), model=model, model_args=model_args)))
    
    results = await asyncio.gather(*tasks)

    return results

def none_or_int(value):
    if value.lower() == "none":
        return None
    return int(value)

async def main():
    load_dotenv() 

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to evaluation data in json", required=True)
    parser.add_argument("-k", "--openai-key", type=str, help="OpenAI API Key")
    parser.add_argument("-ia", "--is-openai-azure", action="store_true", help="If OpenAI on Azure")
    parser.add_argument("-m", "--model", type=str, help="Model to use for evaluation", default="gpt-4")
    parser.add_argument("-t", "--temperature", type=float, help="Temperature for generation", default=0.0)
    parser.add_argument("-g", "--max-tokens", type=none_or_int, help="Max tokens for generation", default=40)
    parser.add_argument("-p", "--top-p", type=float, help="Top p for generation", default=1)
    parser.add_argument("-fp", "--frequency-penalty", type=float, help="Frequency penalty for generation", default=0)
    parser.add_argument("-pp", "--presence-penalty", type=float, help="Presence penalty for generation", default=0)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory for evaluation results", default="outputs")
    parser.add_argument("-n", "--num-samples", type=int, help="Number of samples to evaluate", default=0)
    parser.add_argument("-i", "--ignore-path", type=str, help="Path to already evaluated data", default=None)
    parser.add_argument("-c", "--cache-dir", type=str, help="Cache directory for model", default="~/.cache")
    parser.add_argument("-mp", "--model-path", type=str, help="Model path to use for evaluation", default="gpt2")
    parser.add_argument("-tp", "--tokenizer-path", type=str, help="Tokenizer path to use for evaluation", default="gpt2")
    parser.add_argument("-b", "--batch-size", type=int, help="Batch size for evaluation", default=1)
    
    args = parser.parse_args()
    
    if args.model in API_MODELS:
        if args.is_openai_azure:
            endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT", "https://sigturk-openai.openai.azure.com/")
            client = AsyncAzureOpenAI(
                api_key = args.openai_key if args.openai_key is not None else os.getenv("AZURE_OPENAI_API_KEY"),
                api_version = '2024-02-15-preview',
                azure_endpoint=endpoint
            )
        else:
            client = AsyncOpenAI(api_key=args.openai_key if args.openai_key is not None else os.getenv("OPENAI_API_KEY"))
        
    input_data = read_json(args.datapath)
    data = input_data["data"]
    
    ignore_map = {}

    if args.ignore_path is not None:
        ignore_data = read_json(args.ignore_path)
        
        for sample in ignore_data["data"]:
            ignore_map[sample["id"]] = sample

    if args.num_samples > 0:
        data = data[:int(args.num_samples)]

    outputs = {
        "metadata": {
            "datapath": args.datapath,
            "size": len(data),
            "model": args.model,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "top_p": args.top_p,
            "frequency_penalty": args.frequency_penalty,
            "presence_penalty": args.presence_penalty
        },
        "metrics": {},
        "data": data
    }

    pathlib.Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    datapath = pathlib.Path(args.datapath)
    unique_id = generate_unique_id()
    output_path = os.path.join(args.output_dir, f"{datapath.stem}_{args.model}_{unique_id}.json")
    error_path = os.path.join(args.output_dir, f"{datapath.stem}_{args.model}_{unique_id}_errors.txt")

    print(f"Writing to {output_path}")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if args.model not in API_MODELS and args.model_path:
        model, tokenizer = load_model(model_path=args.model_path, tokenizer_path=args.tokenizer_path, cache_dir=args.cache_dir, device=device)

    model_args = {
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "top_p": args.top_p,
        "frequency_penalty": args.frequency_penalty,
        "presence_penalty": args.presence_penalty
    }

    for batch in tqdm(batched(data, size=args.batch_size), total=math.ceil(len(data)/args.batch_size)):
        try:
            filtered_batch = []

            for sample in batch:
                if "id" in sample and sample["id"] in ignore_map:
                    ignore_instance = ignore_map[sample["id"]]
                    if "model_output" in ignore_instance:
                        sample.update(ignore_instance)
                        continue
                
                if "model_output" in sample:
                    continue
                
                filtered_batch.append(sample)

            results = []

            if args.model in API_MODELS:
                if args.model in CHAT_COMPLETION_MODELS:
                    results = await batch_chat_completion(client, filtered_batch, args.model, model_args)
                elif args.model in TEXT_COMPLETION_MODELS:
                    results = await batch_text_completion(client, filtered_batch, args.model, model_args)
                else:
                    raise ValueError(f"Model {args.model} not supported")

                for sample, result in zip(filtered_batch, results):
                    sample["model_output"] = result.text
                    sample["usage"] = result.usage
            else:
                perplexity = evaluate_lm(sample["prompt"], model, tokenizer, device=device)
                sample["perplexity"] = perplexity
            
            write_json(outputs, output_path, ensure_ascii=False)
        except Exception as e:
            with open(error_path, "a") as error_file:
                error_file.write(f"Error for sample {sample['id']}: {str(e)}\n")
                error_file.write(traceback.format_exc())
                error_file.write("\n")

    write_json(outputs, output_path, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(main())
