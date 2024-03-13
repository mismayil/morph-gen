import argparse
from sklearn.metrics import accuracy_score
from tqdm import tqdm
import pathlib
from itertools import permutations
from collections import defaultdict
import re

from utils import read_json, write_json, find_json_files, MODEL_COSTS, num_tokens_from_string

def get_prediction(ref_response, model_response, template):
    if template in ["bfill"]:
        model_response = [word.strip().strip("'").strip('"').strip() for word in model_response.strip("[]").split(",")]
        pred = 1 if str(ref_response) == str(model_response) else 0
    elif template.startswith("morph_gen"):
        pred = 1 if str(ref_response) == str(model_response).strip() else 0
    elif template.startswith("morph_disc"):
        res = model_response.strip()
        if re.fullmatch(r"\d+\s*\..*", model_response.strip()):
            res = model_response.split(".")[0].strip()
        pred = 1 if str(ref_response) == res else 0
    else:
        raise ValueError(f"Template {template} not supported for evaluation.")

    return pred

def is_faithful(result, ref_response, model_response, template, separator=""):
    if template.startswith("morph_disc"):
        if re.fullmatch(r"\d+", model_response.strip()):
            return True
        return False
    
    if template.startswith("morph_gen_order"):
        if re.fullmatch(r"(\d+,\s*)+\d+", model_response.strip()):
            return True
        return False

    if template.startswith("morph_gen"):
        if len(model_response) != len(ref_response):
            return False
        
        suffix_perms = list(permutations(result["suffixes"]))
        
        for suffix_perm in suffix_perms:
            root_derivation = result["root"] + separator + separator.join(suffix_perm)
            if root_derivation == model_response:
                return True
    
    return False

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

def compute_metrics(results, compute_usage=False, separator="", frequency_path=None):
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

    len_suffix_accuracy = defaultdict(list)
    len_suffix_faithful = defaultdict(list)
    freq_bins = [(0, 10), (10, 100), (100, 1000), (1000,)]
    freq_accuracy = defaultdict(list)
    freq_faithful = defaultdict(list)
    num_freq_samples = defaultdict(dict)

    frequencies = None

    if frequency_path:
        frequencies = read_json(frequency_path)

    for result in results["data"]:
        gold_response_attr = "reference"
        model_response_attr = "model_output"

        if model_response_attr in result:
            ref = 1
            pred = get_prediction(result[gold_response_attr], result[model_response_attr], result["template"])
            references.append(ref)
            predictions.append(pred)
            result["correct"] = ref == pred
            result["faithful"] = is_faithful(result, result[gold_response_attr], result[model_response_attr], result["template"], separator=separator)
            len_suffix_accuracy[len(result["suffixes"])].append(result["correct"])
            len_suffix_faithful[len(result["suffixes"])].append(result["faithful"])

            if frequencies:
                word_freq = frequencies.get("".join([result["root"]]+result["suffixes"]), 0)
                for freq_bin in freq_bins:
                    if word_freq >= freq_bin[0] and (len(freq_bin) == 1 or word_freq < freq_bin[1]):
                        freq_accuracy[str(freq_bin)].append(result["correct"])
                        freq_faithful[str(freq_bin)].append(result["faithful"])
                        if len(result["suffixes"]) not in num_freq_samples[str(freq_bin)]:
                            num_freq_samples[str(freq_bin)][len(result["suffixes"])] = 0
                        num_freq_samples[str(freq_bin)][len(result["suffixes"])] += 1
                        break

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

    metrics["accuracy"] = accuracy_score(references, predictions)
    metrics["faithfulness"] = sum([1 for result in results["data"] if result.get("faithful")]) / len(results["data"])
    
    len_suffix_accuracy = dict(sorted(len_suffix_accuracy.items(), key=lambda item: item[0]))
    len_suffix_faithful = dict(sorted(len_suffix_faithful.items(), key=lambda item: item[0]))
    
    metrics["accuracy_by_suffix_len"] = {k: sum(v) / len(v) for k, v in len_suffix_accuracy.items()}
    metrics["faithfulness_by_suffix_len"] = {k: sum(v) / len(v) for k, v in len_suffix_faithful.items()}
    metrics["num_samples_by_suffix_len"] = {k: len(v) for k, v in len_suffix_accuracy.items()}
    
    if frequencies:
        freq_accuracy = dict(sorted(freq_accuracy.items(), key=lambda item: item[0]))
        freq_faithful = dict(sorted(freq_faithful.items(), key=lambda item: item[0]))
        metrics["accuracy_by_frequency"] = {k: sum(v) / len(v) for k, v in freq_accuracy.items()}
        metrics["faithfulness_by_frequency"] = {k: sum(v) / len(v) for k, v in freq_faithful.items()}
        num_freq_samples = dict(sorted(num_freq_samples.items(), key=lambda item: item[0]))
        num_freq_samples = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in num_freq_samples.items()}
        metrics["num_samples_by_frequency"] = num_freq_samples

    if compute_usage:
        metrics["usage"] = usage
        metrics["cost"] = cost

    return metrics

def report_metrics(results_files, compute_usage=False, separator="", frequency_path=None):
    for results_file in tqdm(results_files, total=len(results_files), desc="Reporting metrics"):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                metrics = compute_metrics(results, compute_usage=compute_usage, separator=separator, frequency_path=frequency_path)
                results["metrics"].update(metrics)
                write_json(results, results_file, ensure_ascii=False)
        except Exception as e:
            print(results_file)
            raise e

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("-u", "--compute-usage", action="store_true", help="Compute usage metrics", default=False)
    parser.add_argument("-t", "--separator", type=str, default="", help="Separator to use between morphemes. Defaults to empty string.")
    parser.add_argument("-f", "--frequency-path", type=str, help="Path to unigram frequency file", default=None)

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_json_files(args.results_path))

    report_metrics(files_to_process, args.compute_usage, args.separator, args.frequency_path)

if __name__ == "__main__":
    main()