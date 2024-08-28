import argparse
from sklearn.metrics import recall_score, precision_score, f1_score
from tqdm import tqdm
import pathlib
from itertools import permutations, product
from collections import defaultdict, Counter
import re
import numpy as np
from statistics import mean
import random

from utils import read_json, write_json, find_files, compute_usage

ANSWER_MAP = {
    "en": {"yes": 1, "no": 0},
    "tr": {"evet": 1, "hayır": 0}
}

def _get_template_lang(template):
    return template.split("_")[-1]

def _get_affixes(sample):
    return sample.get("prefixes", []) + sample.get("suffixes", [])

def get_prediction(sample, model_response, template):
    lang = _get_template_lang(template)
    if template.startswith("morph_disc_mcq"):
        pred = str(model_response).strip()
        if re.fullmatch(r"\d+\s*\..*", model_response.strip()):
            pred = model_response.split(".")[0].strip()
        return pred
    
    if template.startswith("morph_disc_pp"):
        return sample["perplexity"]

    if template.startswith("morph_gen_cot") or template.startswith("morph_disc_cot"):
        preds = re.findall("<.*>(?P<pred>.*)</.*>", model_response)
        if preds:
            pred = preds[-1].strip().lower()
            if template.startswith("morph_disc"):
                return ANSWER_MAP[lang].get(pred, 0)
            return pred

    if template.startswith("morph_disc_bin") or template.startswith("morph_disc"):
        pred = str(model_response).strip().lower()
        return ANSWER_MAP[lang].get(pred, 0)

    pred = str(model_response).strip().lower()
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
        
        prefixes = result.get("prefixes", [])
        suffixes = result.get("suffixes", [])
        prefix_perms = list(permutations(prefixes))
        suffix_perms = list(permutations(suffixes))

        if prefix_perms and suffix_perms:
            affix_perms = product(prefix_perms, suffix_perms)
        elif prefix_perms:
            affix_perms = prefix_perms
        elif suffix_perms:
            affix_perms = suffix_perms
        
        for prefix_perm, suffix_perm in affix_perms:
            root_derivation = separator.join(prefix_perm) + separator + result["root"] + separator + separator.join(suffix_perm)
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

def _normalize_morphemes(morpheme_dict):
    if morpheme_dict:
        normalized_dict = {}
        for k, v in morpheme_dict.items():
            composition = k.replace("+", "")
            normalized_dict[composition] = max(v, normalized_dict.get(composition, 0))
        return normalized_dict

def _merge_morpheme_dicts(dict1, dict2):
    if dict1 and dict2:
        merged_dict = dict1.copy()
        for k, v in dict2.items():
            merged_dict[k] = max(v, merged_dict.get(k, 0))
        return merged_dict

def compute_metrics(results, report_usage=True, separator="", frequency_path=None):
    metrics = {}
    results_by_affix_len = defaultdict(dict)
    accuracy_by_affix_len = defaultdict(list)
    faithful_by_affix_len = defaultdict(list)

    random_accuracy_by_affix_len = defaultdict(list)
    majority_accuracy_by_affix_len = defaultdict(list)

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

    freq_bins = [(0, 10), (10, 100), (100, 1000), (1000,)]
    ood_bins = [(0, 25), (25, 50), (50, 75), (75, 100)]
    
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

    if frequency_path:
        frequencies = read_json(frequency_path)
        unigram_freqs = frequencies.get("roots")
        suffix_freqs = _merge_morpheme_dicts(_normalize_morphemes(frequencies.get("morpheme_compositions")), frequencies.get("morphemes"))
        meta_suffix_freqs = _merge_morpheme_dicts(_normalize_morphemes(frequencies.get("meta_morpheme_compositions")), frequencies.get("meta_morphemes"))

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
    result_map = {}
    ref_response_attr = "reference"
    model_response_attr = "model_output"
    majority_pred = 0

    for result in results["data"]:
        num_affixes = len(_get_affixes(result))
        result_map[result["id"]] = result

        if model_response_attr in result:
            ref = get_reference(result, result[ref_response_attr], result["template"])
            pred = get_prediction(result, result[model_response_attr], result["template"])
            random_pred = np.random.choice([0, 1])
            
            if result["template"].startswith("morph_disc") and not result["template"].startswith("morph_disc_mcq"):
                if result["id"] not in results_by_affix_len[num_affixes]:
                    results_by_affix_len[num_affixes][result["id"]] = {"references": [], "predictions": [],
                                                                       "random_predictions": [], "majority_predictions": []}
                results_by_affix_len[num_affixes][result["id"]]["references"].append(ref)
                results_by_affix_len[num_affixes][result["id"]]["predictions"].append(pred)
                results_by_affix_len[num_affixes][result["id"]]["random_predictions"].append(random_pred)
                results_by_affix_len[num_affixes][result["id"]]["majority_predictions"].append(majority_pred)

            result["correct"] = ref == pred
            result["prediction"] = pred
            result["faithful"] = is_faithful(result, result[ref_response_attr], result[model_response_attr], result["template"], separator=separator)
            # result["soft_accuracy"] = get_soft_accuracy(result, result[ref_response_attr], result[model_response_attr], result["template"])
            accuracy_by_affix_len[num_affixes].append(result["correct"])
            faithful_by_affix_len[num_affixes].append(result["faithful"])
            random_accuracy_by_affix_len[num_affixes].append(ref == random_pred)
            majority_accuracy_by_affix_len[num_affixes].append(ref == majority_pred)

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

    def _compute_metric(results_by_id, metric, pred_attr="predictions", strategy="normal", n=None):
        result_by_id_metrics = {}

        for result_id, result in results_by_id.items():
            references = result["references"]
            predictions = result[pred_attr]
            ood_bin = ood_bins[0]

            if template.startswith("morph_disc_pp"):
                predictions = [0] * len(references)
                min_pp_index = np.argmin(result[pred_attr])
                predictions[min_pp_index] = 1
                full_result = result_map[result_id]
                ood_pct = full_result.get("ood_pct", 0)
                ood_bin_index = [obin[0] <= ood_pct <= obin[1] for obin in ood_bins].index(True)
                ood_bin = ood_bins[ood_bin_index]

            if strategy == "normal":
                result_by_id_metrics[(result_id, str(ood_bin))] = metric(references, predictions, average="macro", zero_division=0)
            elif strategy == "two_way":
                pos_ref_index = references.index(1)
                if n is None or n <= 0 or n > len(references)-1:
                    n = len(references)-1
                neg_ref_indices = random.sample([i for i, ref in enumerate(references) if ref == 0], n)
                two_way_results = []
                
                for i in neg_ref_indices:
                    two_way_results.append(metric([references[pos_ref_index], references[i]], [predictions[pos_ref_index], predictions[i]], average="macro", zero_division=0))

                result_by_id_metrics[(result_id, str(ood_bin))] = mean(two_way_results) if two_way_results else metric(references, predictions, average="macro", zero_division=0)
            else:
                raise ValueError("Invalid strategy")

        return result_by_id_metrics

    def _compute_coherence(results_by_id, pred_attr="predictions"):
        coherence = {}

        for result_id, result in results_by_id.items():
            references = result["references"]
            predictions = result[pred_attr]
    
            if template.startswith("morph_disc_pp"):
                predictions = [0] * len(references)
                min_pp_index = np.argmin(result[pred_attr])
                predictions[min_pp_index] = 1

            coherence[result_id] = int(references == predictions)
        
        return mean(coherence.values())

    def _aggregate_by_ood_bin(metric_results):
        ood_results = {}
        for obin in ood_bins:
            ood_bin_values = [value for (result_id, ood_bin), value in metric_results.items() if str(ood_bin) == str(obin)]
            ood_results[str(obin)] = mean(ood_bin_values) if ood_bin_values else 0
        return ood_results

    def _sort_by_key(results_by_key):
        return dict(sorted(results_by_key.items(), key=lambda item: item[0]))

    def _compute_f1_metrics(results, results_by_affix_len, pred_attr="predictions", strategy="normal", n=None):
        f1_metrics = {}
        recall_by_affix_len = {affix_len: _compute_metric(results_by_affix_len[affix_len], recall_score, pred_attr=pred_attr, strategy=strategy, n=n) for affix_len in results_by_affix_len}
        precision_by_affix_len = {affix_len: _compute_metric(results_by_affix_len[affix_len], precision_score, pred_attr=pred_attr, strategy=strategy, n=n) for affix_len in results_by_affix_len}
        f1_by_affix_len = {affix_len: _compute_metric(results_by_affix_len[affix_len], f1_score, pred_attr=pred_attr, strategy=strategy, n=n) for affix_len in results_by_affix_len}
        
        f1_metrics["recall_by_affix_len"] = {affix_len: mean(recall_by_affix_len[affix_len].values()) for affix_len in recall_by_affix_len}
        f1_metrics["recall_by_affix_len"] = _sort_by_key(f1_metrics["recall_by_affix_len"])
        
        f1_metrics["precision_by_affix_len"] = {affix_len: mean(precision_by_affix_len[affix_len].values()) for affix_len in precision_by_affix_len}
        f1_metrics["precision_by_affix_len"] = _sort_by_key(f1_metrics["precision_by_affix_len"])
        
        f1_metrics["f1_by_affix_len"] = {affix_len: mean(f1_by_affix_len[affix_len].values()) for affix_len in f1_by_affix_len}
        f1_metrics["f1_by_affix_len"] = _sort_by_key(f1_metrics["f1_by_affix_len"])

        f1_metrics["recall"] = mean(f1_metrics["recall_by_affix_len"].values())
        f1_metrics["precision"] = mean(f1_metrics["precision_by_affix_len"].values())
        f1_metrics["f1"] = mean(f1_metrics["f1_by_affix_len"].values())

        f1_metrics["coherence_by_affix_len"] = {affix_len: _compute_coherence(results_by_affix_len[affix_len], pred_attr=pred_attr) for affix_len in results_by_affix_len}
        f1_metrics["coherence_by_affix_len"] = _sort_by_key(f1_metrics["coherence_by_affix_len"])
        f1_metrics["coherence"] = mean(f1_metrics["coherence_by_affix_len"].values())

        if results["data"][0].get("ood_pct") is not None:
            f1_metrics["recall_by_ood_bin_by_affix_len"] = {affix_len: _aggregate_by_ood_bin(recall_by_affix_len[affix_len]) for affix_len in recall_by_affix_len}
            f1_metrics["recall_by_ood_bin_by_affix_len"] = _sort_by_key(f1_metrics["recall_by_ood_bin_by_affix_len"])

            f1_metrics["precision_by_ood_bin_by_affix_len"] = {affix_len: _aggregate_by_ood_bin(precision_by_affix_len[affix_len]) for affix_len in precision_by_affix_len}
            f1_metrics["precision_by_ood_bin_by_affix_len"] = _sort_by_key(f1_metrics["precision_by_ood_bin_by_affix_len"])

            f1_metrics["f1_by_ood_bin_by_affix_len"] = {affix_len: _aggregate_by_ood_bin(f1_by_affix_len[affix_len]) for affix_len in f1_by_affix_len}
            f1_metrics["f1_by_ood_bin_by_affix_len"] = _sort_by_key(f1_metrics["f1_by_ood_bin_by_affix_len"])
    
        return f1_metrics

    metrics["random_baseline"] = {}
    metrics["majority_baseline"] = {}
    metrics["random_two_way"] = {}
    metrics["average_two_way"] = {}

    if results_by_affix_len:
        metrics.update(_compute_f1_metrics(results, results_by_affix_len))

        metrics["random_baseline"].update(_compute_f1_metrics(results, results_by_affix_len, pred_attr="random_predictions"))
        metrics["majority_baseline"].update(_compute_f1_metrics(results, results_by_affix_len, pred_attr="majority_predictions"))

        metrics["random_two_way"].update(_compute_f1_metrics(results, results_by_affix_len, pred_attr="predictions", strategy="two_way", n=1))
        metrics["average_two_way"].update(_compute_f1_metrics(results, results_by_affix_len, pred_attr="predictions", strategy="two_way", n=None))

    # metrics["soft_accuracy"] = sum([result.get("soft_accuracy", 0) for result in results["data"]]) / len(results["data"])
    
    accuracy_by_affix_len = _sort_by_key(accuracy_by_affix_len)
    faithful_by_affix_len = _sort_by_key(faithful_by_affix_len)
    random_accuracy_by_affix_len = _sort_by_key(random_accuracy_by_affix_len)
    majority_accuracy_by_affix_len = _sort_by_key(majority_accuracy_by_affix_len)
    
    metrics["accuracy_by_affix_len"] = {k: sum(v) / len(v) for k, v in accuracy_by_affix_len.items()}
    metrics["faithfulness_by_affix_len"] = {k: sum(v) / len(v) for k, v in faithful_by_affix_len.items()}
    metrics["accuracy"] = mean(metrics["accuracy_by_affix_len"].values())
    metrics["faithfulness"] = mean(metrics["faithfulness_by_affix_len"].values())
    # metrics["soft_accuracy_by_suffix_len"] = {k: sum([result.get("soft_accuracy", 0) for result in results["data"] if len(result["suffixes"]) == k]) / len([result for result in results["data"] if len(result["suffixes"]) == k]) for k in accuracy_by_affix_len}
    metrics["num_samples_by_affix_len"] = {k: len(v) for k, v in accuracy_by_affix_len.items()}

    metrics["random_baseline"]["accuracy_by_affix_len"] = {k: sum(v) / len(v) for k, v in random_accuracy_by_affix_len.items()}
    metrics["majority_baseline"]["accuracy_by_affix_len"] = {k: sum(v) / len(v) for k, v in majority_accuracy_by_affix_len.items()}
    
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

    metrics["num_samples"] = len(results["data"])

    return metrics

def report_metrics(results_files, report_usage=True, separator="", frequency_path=None):
    for results_file in tqdm(results_files, total=len(results_files), desc="Reporting metrics"):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                metrics = compute_metrics(results, report_usage=report_usage, separator=separator, frequency_path=frequency_path)
                results["metrics"] = metrics
                write_json(results, results_file, ensure_ascii=False)
        except Exception as e:
            print(results_file)
            raise e

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("-u", "--report-usage", action="store_true", help="Report usage metrics", default=True)
    parser.add_argument("-t", "--separator", type=str, default="", help="Separator to use between morphemes. Defaults to empty string.")
    parser.add_argument("-f", "--frequency-path", type=str, help="Path to frequency file", default=None)

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_files(args.results_path))

    report_metrics(files_to_process, args.report_usage, args.separator, args.frequency_path)

if __name__ == "__main__":
    main()