import argparse
from sklearn.metrics import recall_score, precision_score, f1_score
from tqdm import tqdm
import pathlib
from itertools import permutations
from collections import defaultdict
import re
import numpy as np

from utils import read_json, write_json, find_files, MODEL_COSTS, num_tokens_from_string

ANSWER_MAP = {
    "en": {"yes": 1, "no": 0},
    "tr": {"evet": 1, "hayır": 0}
}

def _get_template_lang(template):
    return template.split("_")[-1]

def get_prediction(sample, model_response, template):
    pred = str(model_response).strip().lower()
    
    if template.startswith("morph_disc_mcq"):
        pred = model_response.strip()
        if re.fullmatch(r"\d+\s*\..*", model_response.strip()):
            pred = model_response.split(".")[0].strip()
        return pred
    
    if template.startswith("morph_disc_pp"):
        return sample["perplexity"]

    if template.startswith("morph_disc_bin") or template.startswith("morph_disc"):
        return ANSWER_MAP[_get_template_lang(template)][pred]

    return pred

def get_reference(sample, ref_response, template):
    ref = str(ref_response).strip().lower()
    
    if template.startswith("morph_disc_mcq"):
        return ref

    if template.startswith("morph_disc_bin") or template.startswith("morph_disc"):
        return ANSWER_MAP[_get_template_lang(template)][ref]

    return ref

def is_faithful(result, ref_response, model_response, template, separator=""):
    if template.startswith("morph_disc"):
        if model_response and re.fullmatch(r"\d+", model_response.strip()):
            return True
        return False
    
    if template.startswith("morph_gen_order"):
        if model_response and re.fullmatch(r"(\d+,\s*)+\d+", model_response.strip()):
            return True
        return False

    if template.startswith("morph_gen"):
        if model_response and len(model_response) != len(ref_response):
            return False
        
        suffix_perms = list(permutations(result["suffixes"]))
        
        for suffix_perm in suffix_perms:
            root_derivation = result["root"] + separator + separator.join(suffix_perm)
            if root_derivation == model_response:
                return True
    
    return False

def get_soft_accuracy(result, ref_response, model_response, template):
    # TODO: Fix this
    if template.startswith("morph_gen"):
        if ref_response == model_response:
            return 1
        
        points = 0

        if model_response.startswith(result["root"]):
            for i, suffix in enumerate(result["suffixes"]):
                if model_response.startswith(result["root"] + "".join(result["suffixes"][:i+1])):
                    points += 1
                else:
                    points = 0
                    break
        return points / len(result["suffixes"])

    return 1

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

def compute_metrics(results, report_usage=False, separator="", unigram_freq_path=None, suffix_freq_path=None, meta_suffix_freq_path=None):
    metrics = {}
    results_by_suffix_len = defaultdict(dict)

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
    
    unigram_freq_accuracy = defaultdict(list)
    unigram_freq_faithful = defaultdict(list)
    num_unigram_freq_samples = defaultdict(dict)

    suffix_freq_accuracy = defaultdict(list)
    suffix_freq_faithful = defaultdict(list)
    num_suffix_freq_samples = defaultdict(dict)

    meta_suffix_freq_accuracy = defaultdict(list)
    meta_suffix_freq_faithful = defaultdict(list)
    num_meta_suffix_freq_samples = defaultdict(dict)

    suffix_freq_by_len_accuracy = defaultdict(dict)
    suffix_freq_by_len_faithful = defaultdict(dict)
    suffix_freq_by_len_samples = defaultdict(dict)

    meta_suffix_freq_by_len_accuracy = defaultdict(dict)
    meta_suffix_freq_by_len_faithful = defaultdict(dict)
    meta_suffix_freq_by_len_samples = defaultdict(dict)

    suffix_len_by_freq_accuracy = defaultdict(dict)
    suffix_len_by_freq_faithful = defaultdict(dict)

    meta_suffix_len_by_freq_accuracy = defaultdict(dict)
    meta_suffix_len_by_freq_faithful = defaultdict(dict)

    unigram_freqs = None
    suffix_freqs = None
    meta_suffix_freqs = None

    if unigram_freq_path:
        unigram_freqs = read_json(unigram_freq_path)
    
    if suffix_freq_path:
        suffix_freqs = read_json(suffix_freq_path)
    
    if meta_suffix_freq_path:
        meta_suffix_freqs = read_json(meta_suffix_freq_path)

    def _update_freq_metrics(freq, freq_accuracy, freq_faithful, num_freq_samples, result, suffix_key="suffixes"):
        for freq_bin in freq_bins:
            if freq >= freq_bin[0] and (len(freq_bin) == 1 or freq < freq_bin[1]):
                suffix_len = len(result[suffix_key])
                freq_bin = str(freq_bin)

                freq_accuracy[freq_bin].append(result["correct"])
                freq_faithful[freq_bin].append(result["faithful"])
                
                if suffix_len not in num_freq_samples[freq_bin]:
                    num_freq_samples[freq_bin][suffix_len] = 0
                num_freq_samples[freq_bin][suffix_len] += 1
                
                break

    def _update_freq_by_len_metrics(freq, freq_by_len_accuracy, freq_by_len_faithful, num_freq_by_len_samples, result, suffix_key="suffixes"):
        for freq_bin in freq_bins:
            if freq >= freq_bin[0] and (len(freq_bin) == 1 or freq < freq_bin[1]):
                suffix_len = len(result[suffix_key])
                freq_bin = str(freq_bin)

                if suffix_len not in freq_by_len_accuracy:
                    freq_by_len_accuracy[suffix_len] = defaultdict(list)
                    freq_by_len_faithful[suffix_len] = defaultdict(list)
                    num_freq_by_len_samples[suffix_len] = defaultdict(int)

                freq_by_len_accuracy[suffix_len][freq_bin].append(result["correct"])
                freq_by_len_faithful[suffix_len][freq_bin].append(result["faithful"])
                
                if freq_bin not in num_freq_by_len_samples[suffix_len]:
                    num_freq_by_len_samples[suffix_len][freq_bin] = 0
                num_freq_by_len_samples[suffix_len][freq_bin] += 1
                
                break

    def _update_len_by_freq_metrics(freq, len_by_freq_accuracy, len_by_freq_faithful, result, suffix_key="suffixes"):
        for freq_bin in freq_bins:
            if freq >= freq_bin[0] and (len(freq_bin) == 1 or freq < freq_bin[1]):
                suffix_len = len(result[suffix_key])
                freq_bin = str(freq_bin)

                if freq_bin not in len_by_freq_accuracy:
                    len_by_freq_accuracy[freq_bin] = defaultdict(list)
                    len_by_freq_faithful[freq_bin] = defaultdict(list)

                len_by_freq_accuracy[freq_bin][suffix_len].append(result["correct"])
                len_by_freq_faithful[freq_bin][suffix_len].append(result["faithful"])
                
                break

    def _add_freq_metrics(metrics, freq_accuracy, freq_faithful, num_freq_samples, keyword="unigram"):
        freq_accuracy = dict(sorted(freq_accuracy.items(), key=lambda item: item[0]))
        freq_faithful = dict(sorted(freq_faithful.items(), key=lambda item: item[0]))
        metrics[f"accuracy_by_{keyword}_freq"] = {k: sum(v) / len(v) for k, v in freq_accuracy.items()}
        metrics[f"faithfulness_by_{keyword}_freq"] = {k: sum(v) / len(v) for k, v in freq_faithful.items()}
        num_freq_samples = dict(sorted(num_freq_samples.items(), key=lambda item: item[0]))
        num_freq_samples = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in num_freq_samples.items()}
        metrics[f"num_samples_by_{keyword}_freq"] = num_freq_samples

    def _add_freq_by_len_metrics(metrics, freq_by_len_accuracy, freq_by_len_faithful, num_freq_by_len_samples, keyword="unigram"):
        freq_by_len_accuracy = dict(sorted(freq_by_len_accuracy.items(), key=lambda item: item[0]))
        freq_by_len_accuracy = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in freq_by_len_accuracy.items()}
        freq_by_len_faithful = dict(sorted(freq_by_len_faithful.items(), key=lambda item: item[0]))
        freq_by_len_faithful = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in freq_by_len_faithful.items()}
        metrics[f"accuracy_by_{keyword}_freq_by_len"] = {k: {k2: sum(v2) / len(v2) for k2, v2 in v.items()} for k, v in freq_by_len_accuracy.items()}
        metrics[f"faithfulness_by_{keyword}_freq_by_len"] = {k: {k2: sum(v2) / len(v2) for k2, v2 in v.items()} for k, v in freq_by_len_faithful.items()}
        num_freq_by_len_samples = dict(sorted(num_freq_by_len_samples.items(), key=lambda item: item[0]))
        num_freq_by_len_samples = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in num_freq_by_len_samples.items()}
        metrics[f"num_samples_by_{keyword}_freq_by_len"] = num_freq_by_len_samples

    def _add_len_by_freq_metrics(metrics, len_by_freq_accuracy, len_by_freq_faithful, keyword="unigram"):
        len_by_freq_accuracy = dict(sorted(len_by_freq_accuracy.items(), key=lambda item: item[0]))
        len_by_freq_accuracy = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in len_by_freq_accuracy.items()}
        len_by_freq_faithful = dict(sorted(len_by_freq_faithful.items(), key=lambda item: item[0]))
        len_by_freq_faithful = {k: dict(sorted(v.items(), key=lambda item: item[0])) for k, v in len_by_freq_faithful.items()}
        metrics[f"accuracy_by_{keyword}_len_by_freq"] = {k: {k2: sum(v2) / len(v2) for k2, v2 in v.items()} for k, v in len_by_freq_accuracy.items()}
        metrics[f"faithfulness_by_{keyword}_len_by_freq"] = {k: {k2: sum(v2) / len(v2) for k2, v2 in v.items()} for k, v in len_by_freq_faithful.items()}

    template = results["data"][0]["template"]

    for result in results["data"]:
        num_suffixes = len(result["suffixes"])
        ref_response_attr = "reference"
        model_response_attr = "model_output"

        if model_response_attr in result:
            ref = get_reference(result, result[ref_response_attr], result["template"])
            pred = get_prediction(result, result[model_response_attr], result["template"])
            
            if result["template"].startswith("morph_disc") and not result["template"].startswith("morph_disc_mcq"):
                if result["id"] not in results_by_suffix_len[num_suffixes]:
                    results_by_suffix_len[num_suffixes][result["id"]] = {"references": [], "predictions": []}
                results_by_suffix_len[num_suffixes][result["id"]]["references"].append(ref)
                results_by_suffix_len[num_suffixes][result["id"]]["predictions"].append(pred)

            result["correct"] = ref == pred
            result["faithful"] = is_faithful(result, result[ref_response_attr], result[model_response_attr], result["template"], separator=separator)
            # result["soft_accuracy"] = get_soft_accuracy(result, result[ref_response_attr], result[model_response_attr], result["template"])
            len_suffix_accuracy[num_suffixes].append(result["correct"])
            len_suffix_faithful[num_suffixes].append(result["faithful"])

            if unigram_freqs and result.get("root"):
                word_freq = unigram_freqs.get("".join([result["root"]]+result["suffixes"]), 0)
                _update_freq_metrics(word_freq, unigram_freq_accuracy, unigram_freq_faithful, num_unigram_freq_samples, result)

            if suffix_freqs and result.get("suffixes"):
                suffix_freq = suffix_freqs.get("".join(result["suffixes"]), 0)
                _update_freq_metrics(suffix_freq, suffix_freq_accuracy, suffix_freq_faithful, num_suffix_freq_samples, result)
                _update_freq_by_len_metrics(suffix_freq, suffix_freq_by_len_accuracy, suffix_freq_by_len_faithful, suffix_freq_by_len_samples, result)
                _update_len_by_freq_metrics(suffix_freq, suffix_len_by_freq_accuracy, suffix_len_by_freq_faithful, result)
            
            if meta_suffix_freqs and result.get("meta_suffixes"):
                meta_suffix_freq = meta_suffix_freqs.get("".join(result["meta_suffixes"]), 0)
                _update_freq_metrics(meta_suffix_freq, meta_suffix_freq_accuracy, meta_suffix_freq_faithful, num_meta_suffix_freq_samples, result, suffix_key="meta_suffixes")
                _update_freq_by_len_metrics(meta_suffix_freq, meta_suffix_freq_by_len_accuracy, meta_suffix_freq_by_len_faithful, meta_suffix_freq_by_len_samples, result, suffix_key="meta_suffixes")
                _update_len_by_freq_metrics(meta_suffix_freq, meta_suffix_len_by_freq_accuracy, meta_suffix_len_by_freq_faithful, result, suffix_key="meta_suffixes")

            if report_usage:
                sample_usage, sample_cost = compute_usage(result, results["metadata"]["model"])

                if sample_usage:
                    usage["prompt_tokens"] += sample_usage["prompt_tokens"]
                    usage["completion_tokens"] += sample_usage["completion_tokens"]
                    usage["total_tokens"] += sample_usage["total_tokens"]

                if sample_cost:
                    cost["input"] += sample_cost["input"]
                    cost["output"] += sample_cost["output"]
                    cost["total"] += sample_cost["total"]

    metrics["accuracy"] = sum([1 for result in results["data"] if result.get("correct")]) / len(results["data"])
    metrics["faithfulness"] = sum([1 for result in results["data"] if result.get("faithful")]) / len(results["data"])

    def _compute_metric(results_by_id, metric):
        result_by_id_metrics = {}

        for result_id, result in results_by_id.items():
            references = result["references"]
            predictions = result["predictions"]
    
            if template.startswith("morph_disc_pp"):
                predictions = [0] * len(references)
                min_pp_index = np.argmin(result["predictions"])
                predictions[min_pp_index] = 1

            result_by_id_metrics[result_id] = metric(references, predictions, average="macro", zero_division=0)
        
        return result_by_id_metrics

    def _compute_coherence(results_by_id):
        coherence = {}

        for result_id, result in results_by_id.items():
            references = result["references"]
            predictions = result["predictions"]
    
            if template.startswith("morph_disc_pp"):
                predictions = [0] * len(references)
                min_pp_index = np.argmin(result["predictions"])
                predictions[min_pp_index] = 1

            coherence[result_id] = int(references == predictions)
        
        return sum(coherence.values()) / len(coherence)

    if results_by_suffix_len:
        recall_by_suffix_len = {suffix_len: _compute_metric(results_by_suffix_len[suffix_len], recall_score) for suffix_len in results_by_suffix_len}
        precision_by_suffix_len = {suffix_len: _compute_metric(results_by_suffix_len[suffix_len], precision_score) for suffix_len in results_by_suffix_len}
        f1_by_suffix_len = {suffix_len: _compute_metric(results_by_suffix_len[suffix_len], f1_score) for suffix_len in results_by_suffix_len}
        
        metrics["recall_by_suffix_len"] = {suffix_len: sum(recall_by_suffix_len[suffix_len].values()) / len(recall_by_suffix_len[suffix_len]) for suffix_len in recall_by_suffix_len}
        metrics["recall_by_suffix_len"] = dict(sorted(metrics["recall_by_suffix_len"].items(), key=lambda item: item[0]))
        
        metrics["precision_by_suffix_len"] = {suffix_len: sum(precision_by_suffix_len[suffix_len].values()) / len(precision_by_suffix_len[suffix_len]) for suffix_len in precision_by_suffix_len}
        metrics["precision_by_suffix_len"] = dict(sorted(metrics["precision_by_suffix_len"].items(), key=lambda item: item[0]))
        
        metrics["f1_by_suffix_len"] = {suffix_len: sum(f1_by_suffix_len[suffix_len].values()) / len(f1_by_suffix_len[suffix_len]) for suffix_len in f1_by_suffix_len}
        metrics["f1_by_suffix_len"] = dict(sorted(metrics["f1_by_suffix_len"].items(), key=lambda item: item[0]))

        metrics["recall"] = sum(metrics["recall_by_suffix_len"].values()) / len(metrics["recall_by_suffix_len"])
        metrics["precision"] = sum(metrics["precision_by_suffix_len"].values()) / len(metrics["precision_by_suffix_len"])
        metrics["f1"] = sum(metrics["f1_by_suffix_len"].values()) / len(metrics["f1_by_suffix_len"])

        metrics["coherence_by_suffix_len"] = {suffix_len: _compute_coherence(results_by_suffix_len[suffix_len]) for suffix_len in results_by_suffix_len}
        metrics["coherence_by_suffix_len"] = dict(sorted(metrics["coherence_by_suffix_len"].items(), key=lambda item: item[0]))
        metrics["coherence"] = sum(metrics["coherence_by_suffix_len"].values()) / len(metrics["coherence_by_suffix_len"])

    # metrics["soft_accuracy"] = sum([result.get("soft_accuracy", 0) for result in results["data"]]) / len(results["data"])
    
    len_suffix_accuracy = dict(sorted(len_suffix_accuracy.items(), key=lambda item: item[0]))
    len_suffix_faithful = dict(sorted(len_suffix_faithful.items(), key=lambda item: item[0]))
    
    metrics["accuracy_by_suffix_len"] = {k: sum(v) / len(v) for k, v in len_suffix_accuracy.items()}
    metrics["faithfulness_by_suffix_len"] = {k: sum(v) / len(v) for k, v in len_suffix_faithful.items()}
    # metrics["soft_accuracy_by_suffix_len"] = {k: sum([result.get("soft_accuracy", 0) for result in results["data"] if len(result["suffixes"]) == k]) / len([result for result in results["data"] if len(result["suffixes"]) == k]) for k in len_suffix_accuracy}
    metrics["num_samples_by_suffix_len"] = {k: len(v) for k, v in len_suffix_accuracy.items()}
    
    if unigram_freqs:
        _add_freq_metrics(metrics, unigram_freq_accuracy, unigram_freq_faithful, num_unigram_freq_samples, keyword="unigram")
    
    if suffix_freqs:
        _add_freq_metrics(metrics, suffix_freq_accuracy, suffix_freq_faithful, num_suffix_freq_samples, keyword="suffix")
        _add_freq_by_len_metrics(metrics, suffix_freq_by_len_accuracy, suffix_freq_by_len_faithful, suffix_freq_by_len_samples, keyword="suffix")
        _add_len_by_freq_metrics(metrics, suffix_len_by_freq_accuracy, suffix_len_by_freq_faithful, keyword="suffix")
    
    if meta_suffix_freqs:
        _add_freq_metrics(metrics, meta_suffix_freq_accuracy, meta_suffix_freq_faithful, num_meta_suffix_freq_samples, keyword="meta_suffix")
        _add_freq_by_len_metrics(metrics, meta_suffix_freq_by_len_accuracy, meta_suffix_freq_by_len_faithful, meta_suffix_freq_by_len_samples, keyword="meta_suffix")
        _add_len_by_freq_metrics(metrics, meta_suffix_len_by_freq_accuracy, meta_suffix_len_by_freq_faithful, keyword="meta_suffix")

    if report_usage:
        metrics["usage"] = usage
        metrics["cost"] = cost

    return metrics

def report_metrics(results_files, report_usage=False, separator="", unigram_freq_path=None, suffix_freq_path=None, meta_suffix_freq_path=None):
    for results_file in tqdm(results_files, total=len(results_files), desc="Reporting metrics"):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                metrics = compute_metrics(results, report_usage=report_usage, separator=separator,
                                          unigram_freq_path=unigram_freq_path, 
                                          suffix_freq_path=suffix_freq_path, 
                                          meta_suffix_freq_path=meta_suffix_freq_path)
                results["metrics"].update(metrics)
                write_json(results, results_file, ensure_ascii=False)
        except Exception as e:
            print(results_file)
            raise e

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("-u", "--report-usage", action="store_true", help="Report usage metrics", default=False)
    parser.add_argument("-t", "--separator", type=str, default="", help="Separator to use between morphemes. Defaults to empty string.")
    parser.add_argument("-uf", "--unigram-freq-path", type=str, help="Path to unigram frequency file", default=None)
    parser.add_argument("-sf", "--suffix-freq-path", type=str, help="Path to suffix frequency file", default=None)
    parser.add_argument("-mf", "--meta-suffix-freq-path", type=str, help="Path to meta suffix frequency file", default=None)

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_files(args.results_path))

    report_metrics(files_to_process, args.report_usage, args.separator, args.unigram_freq_path, args.suffix_freq_path, args.meta_suffix_freq_path)

if __name__ == "__main__":
    main()