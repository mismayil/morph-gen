import argparse
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tqdm import tqdm
import pathlib

from utils import read_json, write_json, find_json_files, MODEL_COSTS, num_tokens_from_string

def get_prediction(ref_response, model_response, template):
    if template in ["bfill"]:
        model_response = [word.strip().strip("'").strip('"').strip() for word in model_response.strip("[]").split(",")]
        pred = 1 if str(ref_response) == str(model_response) else 0
    elif template in ["morph_gen", "morph_disc"]:
        pred = 1 if str(ref_response) == str(model_response).strip() else 0
    else:
        raise ValueError(f"Template {template} not supported for evaluation.")

    return pred

def compute_usage(sample, model):
    if model not in MODEL_COSTS:
        return None, None

    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }

    if "usage" in sample:
        usage = sample["usage"]
    else:
        prompt_tokens = num_tokens_from_string(sample["prompt"], model)
        completion_tokens = num_tokens_from_string(sample["response"], model)
        usage = {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens
        }
    
    input_cost = usage["prompt_tokens"] * MODEL_COSTS[model]["input"]
    output_cost = usage["completion_tokens"] * MODEL_COSTS[model]["output"]

    return usage, {
        "input": input_cost,
        "output": output_cost,
        "total": input_cost + output_cost
    }

def compute_metrics(results, compute_usage=False):
    metrics = {}
    predictions = []
    references = []

    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }

    cost = {
        "input": 0,
        "output": 0,
        "total": 0
    }

    for result in results["data"]:
        gold_response_attr = "reference"
        model_response_attr = "model_output"

        if model_response_attr in result:
            ref = 1
            pred = get_prediction(result[gold_response_attr], result[model_response_attr], result["template"])
            references.append(ref)
            predictions.append(pred)
            result["correct"] = ref == pred
            
            if compute_usage:
                sample_usage, sample_cost = compute_usage(result, results["metadata"]["model"])

                if sample_usage:
                    usage["prompt_tokens"] += sample_usage["prompt_tokens"]
                    usage["completion_tokens"] += sample_usage["completion_tokens"]
                    usage["total_tokens"] += sample_usage["total_tokens"]

                if sample_cost:
                    cost["input"] += sample_cost["input"]
                    cost["output"] += sample_cost["output"]
                    cost["total"] += sample_cost["total"]

    metrics["macro_f1"] = f1_score(references, predictions, average='macro')
    metrics["accuracy"] = accuracy_score(references, predictions)
    metrics["precision"] = precision_score(references, predictions, average='macro')
    metrics["recall"] = recall_score(references, predictions, average='macro')

    if compute_usage:
        metrics["usage"] = usage
        metrics["cost"] = cost

    return metrics

def report_metrics(results_files, compute_usage=False):
    for results_file in tqdm(results_files, total=len(results_files)):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                metrics = compute_metrics(results, compute_usage=compute_usage)
                results["metrics"].update(metrics)
                write_json(results, results_file)
        except Exception as e:
            print(results_file)
            raise e

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("--compute-usage", action="store_true", help="Compute usage metrics", default=False)

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_json_files(args.results_path))

    report_metrics(files_to_process, args.compute_usage)

if __name__ == "__main__":
    main()