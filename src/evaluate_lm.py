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
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable, DeadlineExceeded

logging.basicConfig(stream=sys.stderr, level=logging.WARN)
logger = logging.getLogger(__name__)

from utils import read_json, write_json, generate_unique_id, batched

OPENAI_CHAT_COMPLETION_MODELS = ["gpt-3.5-turbo", "gpt-4", "gpt-4-0125-preview", "gpt-4o-2024-08-06"]
OPENAI_TEXT_COMPLETION_MODELS = ["text-davinci-003"]
OPENAI_MODELS = OPENAI_CHAT_COMPLETION_MODELS + OPENAI_TEXT_COMPLETION_MODELS
GOOGLE_CHAT_COMPLETION_MODELS = ["gemini-1.5-flash", "gemini-1.5-pro"]
GOOGLE_MODELS = GOOGLE_CHAT_COMPLETION_MODELS
CHAT_COMPLETION_MODELS = OPENAI_CHAT_COMPLETION_MODELS + GOOGLE_CHAT_COMPLETION_MODELS
TEXT_COMPLETION_MODELS = OPENAI_TEXT_COMPLETION_MODELS
API_MODELS = OPENAI_MODELS + GOOGLE_MODELS
PERPLEXITY_MODELS = ["gpt-2"]
LLAMA_MODELS = ["tr-llama-8b"]
PORO_MODELS = ["poro-34b"]
AYA_MODELS = ["aya-23-8b", "aya-23-35b"]
AHMA_MODELS = ["ahma-3b", "ahma-7b"]
GEMMA_MODELS = ["gemma-2-2b", "gemma-2-9b", "gemma-2-27b"]
QWEN_MODELS = ["qwen-2.5-7b", "qwen-2.5-14b", "qwen-2.5-32b"]
HF_MODELS = LLAMA_MODELS + PORO_MODELS + AYA_MODELS + AHMA_MODELS + GEMMA_MODELS + QWEN_MODELS

@dataclasses.dataclass
class ModelResponse:
    text: str
    usage: dict = None
    exception: Exception = None

def get_openai_model_args(model_args):
    openai_model_args = {}

    if model_args is not None:
        if "temperature" in model_args:
            openai_model_args["temperature"] = model_args["temperature"]
        if "max_tokens" in model_args:
            openai_model_args["max_tokens"] = model_args["max_tokens"]
        if "top_p" in model_args:
            openai_model_args["top_p"] = model_args["top_p"]
        if "frequency_penalty" in model_args:
            openai_model_args["frequency_penalty"] = model_args["frequency_penalty"]
        if "presence_penalty" in model_args:
            openai_model_args["presence_penalty"] = model_args["presence_penalty"]

    return openai_model_args

@retry(retry=retry_if_exception_type((APITimeoutError, APIConnectionError, RateLimitError, InternalServerError)), wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10), before_sleep=before_sleep_log(logger, logging.DEBUG))
async def openai_chat_completion(client, messages, model="gpt-3.5-turbo", model_args=None):
    openai_model_args = get_openai_model_args(model_args)
    text = ""
    exception = None
    response = await client.chat.completions.create(model=model, messages=messages, **openai_model_args)
    content = response.choices[0].message.content
    
    if content is None:
        exception = f"Finish reason: {response.choices[0].finish_reason}"
    else:
        text = content.strip()
    
    usage = response.usage
    
    return ModelResponse(text, dict(usage), exception)

async def openai_completion(client, prompt, model, model_args=None):
    try:
        if model in OPENAI_CHAT_COMPLETION_MODELS:
            return await openai_chat_completion(client, [{"role": "user", "content": prompt.strip()}], model=model, model_args=model_args)
        raise ValueError(f"Model {model} not supported")
    except Exception as e:
        return ModelResponse("", None, e)

def get_google_model_args(model_args):
    google_model_args = {}

    if model_args is not None:
        if "temperature" in model_args:
            google_model_args["temperature"] = model_args["temperature"]
        if "max_tokens" in model_args:
            google_model_args["max_output_tokens"] = model_args["max_tokens"]
        if "top_p" in model_args:
            google_model_args["top_p"] = model_args["top_p"]
        if "top_k" in model_args:
            google_model_args["top_k"] = model_args["top_k"]

    return google_model_args

@retry(retry=retry_if_exception_type((ResourceExhausted, ServiceUnavailable, DeadlineExceeded)), wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10), before_sleep=before_sleep_log(logger, logging.DEBUG))
async def google_completion(client, prompt, model, model_args=None):
    text = ""
    exception = None

    model = genai.GenerativeModel(model)
    google_model_args = get_google_model_args(model_args)
    config = genai.GenerationConfig(**google_model_args)
    response = model.generate_content(prompt.strip(), generation_config=config)
    
    try:
        text = response.text.strip()
    except ValueError as e:
        exception = f"Finish reason: {str(response.candidates[0].finish_reason)}"

    return ModelResponse(text, None, exception)

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
    model = AutoModelForCausalLM.from_pretrained(model_path, 
                                                 cache_dir=cache_dir,
                                                 device_map=device,
                                                 torch_dtype=torch.bfloat16)
    model.eval()
    return model, tokenizer

def evaluate_perplexity_model(prompt, model, tokenizer, model_args=None, device="cuda"):
    perplexity = compute_perplexity(prompt, model, tokenizer, device=device)
    return perplexity

def get_hf_model_args(model_args):
    hf_model_args = {}

    if model_args is not None:
        if "temperature" in model_args:
            hf_model_args["temperature"] = model_args["temperature"]
        if "max_tokens" in model_args:
            hf_model_args["max_new_tokens"] = model_args["max_tokens"]
        if "top_p" in model_args:
            hf_model_args["top_p"] = model_args["top_p"]
        if "top_k" in model_args:
            hf_model_args["top_k"] = model_args["top_k"]
        if hf_model_args["top_p"] == 1 and not hf_model_args.get("top_k"):
            hf_model_args["do_sample"] = False
        else:
            hf_model_args["do_sample"] = True
    return hf_model_args

def evaluate_hf_model(prompts, model, tokenizer, model_args=None, device="cuda"):
    hf_model_args = get_hf_model_args(model_args)

    responses = []

    for prompt in prompts:
        messages = [{"role": "user", "content": prompt}]

        input_ids = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
        ).to(device)

        outputs = model.generate(
            input_ids,
            pad_token_id=tokenizer.eos_token_id,
            **hf_model_args
        )
        response = outputs[0][input_ids.shape[-1]:]
        responses.append(ModelResponse(text=tokenizer.decode(response, skip_special_tokens=True)))
    
    return responses

def evaluate_model(prompts, model_name, model, tokenizer, model_args=None, device="cuda"):
    if model_name in HF_MODELS:
        return evaluate_hf_model(prompts, model, tokenizer, model_args=model_args, device=device)
    else:
        raise ValueError(f"Model {model_name} not supported")

async def batch_completion(client, batch, model, model_args):
    tasks = []
    
    for sample in batch:
        if model in OPENAI_MODELS:
            tasks.append(asyncio.create_task(openai_completion(client, sample["prompt"], model=model, model_args=model_args)))
        elif model in GOOGLE_MODELS:
            tasks.append(asyncio.create_task(google_completion(client, sample["prompt"], model=model, model_args=model_args)))
        else:
            raise ValueError(f"Model {model} not supported")
    
    results = await asyncio.gather(*tasks)

    return results

def configure_openai_client(api_key, is_openai_azure=False):
    if is_openai_azure:
        endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT", "https://sigturk-openai.openai.azure.com/")
        client = AsyncAzureOpenAI(
            api_key = api_key if api_key is not None else os.getenv("AZURE_OPENAI_API_KEY"),
            api_version = '2024-02-15-preview',
            azure_endpoint=endpoint
        )
    else:
        client = AsyncOpenAI(api_key=api_key if api_key is not None else os.getenv("OPENAI_API_KEY"))
    
    return client

def configure_google_client(api_key):
    genai.configure(api_key=api_key if api_key is not None else os.getenv("GOOGLE_API_KEY"))
    return None

def none_or_int(value):
    if value.lower() == "none":
        return None
    return int(value)

def _write_error(error_path, sample, exception):
    with open(error_path, "a") as error_file:
        error_file.write(f"Error for sample {sample['id']}: {str(exception)}\n")
        error = "".join(traceback.format_exception(type(exception), value=exception, tb=exception.__traceback__))
        error_file.write(error)
        error_file.write("\n")
    
async def main():
    load_dotenv() 

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to evaluation data in json", required=True)
    parser.add_argument("-a", "--api-key", type=str, help="Model API Key")
    parser.add_argument("-oa", "--openai-azure", action="store_true", help="If OpenAI on Azure")
    parser.add_argument("-m", "--model", type=str, help="Model to use for evaluation", default="gpt-4")
    parser.add_argument("-t", "--temperature", type=float, help="Temperature for generation", default=0.0)
    parser.add_argument("-g", "--max-tokens", type=none_or_int, help="Max tokens for generation", default=40)
    parser.add_argument("-p", "--top-p", type=float, help="Top-p for generation", default=1)
    parser.add_argument("-k", "--top-k", type=float, help="Top-k for generation", default=None)
    parser.add_argument("-fp", "--frequency-penalty", type=float, help="Frequency penalty for generation", default=0)
    parser.add_argument("-pp", "--presence-penalty", type=float, help="Presence penalty for generation", default=0)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory for evaluation results", default="outputs")
    parser.add_argument("-n", "--num-samples", type=int, help="Number of samples to evaluate", default=0)
    parser.add_argument("-c", "--cache-dir", type=str, help="Cache directory for model", default="~/.cache")
    parser.add_argument("-mp", "--model-path", type=str, help="Model path to use for evaluation", default=None)
    parser.add_argument("-tp", "--tokenizer-path", type=str, help="Tokenizer path to use for evaluation", default=None)
    parser.add_argument("-b", "--batch-size", type=int, help="Batch size for evaluation", default=1)
    parser.add_argument("-r", "--resume", action="store_true", help="Resume evaluation from the current file")
    
    args = parser.parse_args()
    client = None

    if args.model in API_MODELS:
        if args.model in OPENAI_MODELS:
            client = configure_openai_client(args.api_key, args.openai_azure)
        elif args.model in GOOGLE_MODELS:
            client = configure_google_client(args.api_key)
        
    input_data = read_json(args.datapath)
    data = input_data["data"]

    if args.num_samples > 0:
        data = data[:int(args.num_samples)]

    outputs = {
        "metadata": {
            **input_data["metadata"],
            "source": args.datapath,
            "size": len(data),
            "model": args.model,
            "model_path": args.model_path,
            "tokenizer_path": args.tokenizer_path,
            "cache_dir": args.cache_dir,
            "batch_size": args.batch_size,
            "openai_azure": args.openai_azure,
            "num_samples": args.num_samples,
            "resume": args.resume,
            "model_args": {
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "top_p": args.top_p,
                "top_k": args.top_k,
                "frequency_penalty": args.frequency_penalty,
                "presence_penalty": args.presence_penalty
            }
        },
        "metrics": {},
        "data": data
    }

    pathlib.Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    datapath = pathlib.Path(args.datapath)
    
    if args.resume:
        output_path = args.datapath
        error_path = args.datapath.replace(".json", "_errors.txt")
    else:
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
        "top_k": args.top_k,
        "frequency_penalty": args.frequency_penalty,
        "presence_penalty": args.presence_penalty
    }

    for batch in tqdm(batched(data, size=args.batch_size), total=math.ceil(len(data)/args.batch_size)):
        try:
            filtered_batch = []

            for sample in batch:
                if "model_output" in sample:
                    continue
                
                filtered_batch.append(sample)

            results = []

            if args.model in API_MODELS:
                results = await batch_completion(client, filtered_batch, args.model, model_args)
                for sample, result in zip(filtered_batch, results):
                    sample["model_output"] = result.text
                    sample["usage"] = result.usage
                    if result.exception is not None:
                        sample["exception"] = str(result.exception)
                        # _write_error(error_path, sample, result.exception)
            elif args.model in PERPLEXITY_MODELS:
                perplexity = evaluate_perplexity_model(sample["prompt"], model, tokenizer, device=device)
                sample["perplexity"] = perplexity
            else:
                results = evaluate_model([sample["prompt"] for sample in filtered_batch], args.model, model, tokenizer, model_args=model_args, device=device)
                for sample, result in zip(filtered_batch, results):
                    sample["model_output"] = result.text
            
            write_json(outputs, output_path, ensure_ascii=False)
        except Exception as e:
            _write_error(error_path, sample, e)

    write_json(outputs, output_path, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(main())
