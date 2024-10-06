import argparse
import pathlib
import random
from collections import Counter

from utils import read_json, write_json

def evaluate_random_baseline(data):
    results = []
    references = list(set([sample["reference"] for sample in data]))

    for sample in data:
        template = sample["template"]
        answer = None

        if "morph_disc" in template:
            answer = random.choice(references)
        elif "morph_gen" in template:
            prefixes = sample.get("prefixes", [])
            suffixes = sample.get("suffixes", [])
            answer = "".join(random.sample(prefixes, len(prefixes))) + sample["root"] + "".join(random.sample(suffixes, len(suffixes)))
        else:
            raise ValueError(f"Invalid template: {template}")

        result = {
            "text": answer
        }

        results.append(result)
    
    return results

def evaluate_majority_baseline(data):
    results = []
    references = Counter([sample["reference"] for sample in data])

    for sample in data:
        template = sample["template"]
        answer = None

        if "morph_disc" in template:
            answer = references.most_common(1)[0][0]
        elif "morph_gen" in template:
            pass
        else:
            raise ValueError(f"Invalid template: {template}")

        result = {
            "text": answer
        }

        results.append(result)
    
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to evaluation data in json", required=True)
    parser.add_argument("-n", "--num-samples", type=int, help="Number of samples to evaluate", default=0)
    parser.add_argument("-m", "--model", type=str, help="Model to use for evaluation", default="random")
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory for evaluation results", default="outputs")

    args = parser.parse_args()
        
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
            "num_samples": args.num_samples,
            "model_args": {}
        },
        "metrics": {},
        "data": data
    }

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    datapath = pathlib.Path(args.datapath)
    output_path = output_dir / f"{datapath.stem}_{args.model}.json"

    if args.model == "random":
        results = evaluate_random_baseline(data)
    elif args.model == "majority":
        results = evaluate_majority_baseline(data)
    else:
        raise ValueError(f"Invalid model: {args.model}")
    
    for sample, result in zip(data, results):
        sample["model_output"] = result["text"]
 
    write_json(outputs, output_path, ensure_ascii=False)

if __name__ == '__main__':
    main()