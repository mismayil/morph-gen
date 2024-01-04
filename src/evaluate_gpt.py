import argparse
import time
from openai import OpenAI, APITimeoutError, APIConnectionError, RateLimitError, InternalServerError
import os
from tqdm import tqdm
import pathlib

from utils import read_json, write_json, generate_unique_id, MODEL_COSTS

CHAT_COMPLETION_MODELS = ["gpt-3.5-turbo", "gpt-4"]
TEXT_COMPLETION_MODELS = ["text-davinci-003"]

def chat_completion(client, messages, model="gpt-3.5-turbo", return_text=True, return_usage=True, model_args=None):
    if model_args is None:
        model_args = {}

    while True:
        try:
            response = client.chat.completions.create(model=model, messages=messages, **model_args)
            text = response.choices[0].message.content.strip()
            usage = response.usage
            
            if return_text and return_usage:
                return text, dict(usage)
            
            if return_text:
                return text
            
            if return_usage:
                return usage

            return response
        except (APITimeoutError, APIConnectionError, RateLimitError, InternalServerError) as e:
            print(f"OpenAI error: {str(e)}. Waiting for 1 minute.")
            time.sleep(60)
            continue

def text_completion(client, prompt, model="text-davinci-003", return_text=True, return_usage=True, model_args=None):
    if model_args is None:
        model_args = {}

    while True:
        try:
            response = client.completion.create(model=model, prompt=prompt, **model_args)
            text = response.choices[0].text.strip()
            usage = response.usage

            if return_text and return_usage:
                return text, dict(usage)
            
            if return_text:
                return text
            
            if return_usage:
                return usage

            return response
        except (APITimeoutError, APIConnectionError, RateLimitError, InternalServerError) as e:
            print(f"OpenAI error: {str(e)}. Waiting for 1 minute.")
            time.sleep(60)
            continue

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to evaluation data in json", required=True)
    parser.add_argument("-k", "--openai-key", type=str, help="OpenAI API Key")
    parser.add_argument("-m", "--model", type=str, help="Model to use for evaluation", default="gpt-3.5-turbo")
    parser.add_argument("-t", "--temperature", type=float, help="Temperature for generation", default=0.3)
    parser.add_argument("-g", "--max-tokens", type=int, help="Max tokens for generation", default=40)
    parser.add_argument("-p", "--top-p", type=float, help="Top p for generation", default=1)
    parser.add_argument("-fp", "--frequency-penalty", type=float, help="Frequency penalty for generation", default=0)
    parser.add_argument("-pp", "--presence-penalty", type=float, help="Presence penalty for generation", default=0)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory for evaluation results", default="outputs")
    parser.add_argument("-n", "--num-samples", type=int, help="Number of samples to evaluate", default=0)
    parser.add_argument("-i", "--ignore-path", type=str, help="Path to already evaluated data", default=None)
    
    args = parser.parse_args()
    
    client = OpenAI(api_key=args.openai_key if args.openai_key is not None else os.getenv("OPENAI_API_KEY"))

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
            "model": args.model,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "top_p": args.top_p,
            "frequency_penalty": args.frequency_penalty,
            "presence_penalty": args.presence_penalty
        },
        "metrics": {
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            },
            "cost": {
                "input": 0,
                "output": 0,
                "total": 0
            }
        },
        "data": data
    }

    pathlib.Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    datapath = pathlib.Path(args.datapath)
    
    output_path = os.path.join(args.output_dir, f"{datapath.stem}_{args.model}_{generate_unique_id()}.json")
    print(f"Writing to {output_path}")
    
    for sample in tqdm(data, total=len(data)):
        if "id" in sample and sample["id"] in ignore_map:
            ignore_instance = ignore_map[sample["id"]]
            if "model_output" in ignore_instance:
                sample.update(ignore_instance)
                continue
    
        if "model_output" in sample:
            continue

        if args.model in CHAT_COMPLETION_MODELS:
            response, usage = chat_completion(client, [{"role": "user", "content": sample["prompt"].strip()}], model=args.model, return_text=True, return_usage=True, model_args={
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "top_p": args.top_p,
                "frequency_penalty": args.frequency_penalty,
                "presence_penalty": args.presence_penalty
            })
        elif args.model in TEXT_COMPLETION_MODELS:
            response, usage = text_completion(client, sample["prompt"].strip(), model=args.model, return_text=True, return_usage=True, model_args={
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "top_p": args.top_p,
                "frequency_penalty": args.frequency_penalty,
                "presence_penalty": args.presence_penalty
            })
        else:
            raise ValueError(f"Model {args.model} not supported for evaluation.")

        sample["model_output"] = response
        sample["usage"] = usage
        outputs["metrics"]["usage"]["prompt_tokens"] += usage["prompt_tokens"]
        outputs["metrics"]["usage"]["completion_tokens"] += usage["completion_tokens"]
        outputs["metrics"]["usage"]["total_tokens"] += usage["total_tokens"]
        
        write_json(outputs, output_path, ensure_ascii=False)

    outputs["metrics"]["cost"]["input"] = outputs["metrics"]["usage"]["prompt_tokens"] * MODEL_COSTS[args.model]["input"]
    outputs["metrics"]["cost"]["output"] = outputs["metrics"]["usage"]["completion_tokens"] * MODEL_COSTS[args.model]["output"]
    outputs["metrics"]["cost"]["total"] = outputs["metrics"]["cost"]["input"] + outputs["metrics"]["cost"]["output"]

    write_json(outputs, output_path, ensure_ascii=False)

if __name__ == "__main__":
    main()
