import sys
import argparse
import pathlib
from tqdm import tqdm
import pandas as pd
import random
import numpy as np
from collections import defaultdict
import re

from utils import read_json, write_json, concatenate_lists
from morphology import decompose_tr, infer_best_decomposition_tr, read_tr_dictionary

LANGUAGES = ["tr", "en"]

def prepare_tr_btwd_json_data(datapath, num_samples=None):
    data = pd.read_csv(datapath)

    if num_samples is not None:
        data = data.sample(num_samples)

    essays = []

    for i, row in data.iterrows():
        if isinstance(row["text"], str):
            raw_texts = re.split("[.?!]\s",row["text"].replace("\r\n", ""))
            texts = []

            for text in raw_texts:
                texts.extend(re.split("\s\s\s\s", text))

            texts = [re.sub("^[A-ZÜÖĞIŞÇİ0-9\-\s.]+$", "", text) for text in texts]
            texts = [re.sub("\s+", " ", text).strip() for text in texts if all(["http" not in text.lower(), "kaynakça" not in text.lower()]) and len(text.strip().split()) > 5]
            
            if len(texts) > 1:
                essays.append({
                    "id": f"bilkent-turkish-writings-{i}",
                    "sentences": texts
                })

    return essays

def postprocess_tr_btwd_data(datapath, num_samples=None):    
    input_data = read_json(datapath)
    data = input_data["data"]

    if num_samples is not None:
        data = dict(random.sample(list(data.items()), num_samples))

    postprocessed_data = []
    tr_dictionary = read_tr_dictionary()

    for root, word_map in tqdm(data.items(), total=len(data.items()), desc="Post-processing btwd data"):
        for word, decompositions in word_map.items():
            if not re.fullmatch(r"\b[^\d\W]+\b", word):
                continue

            if len(decompositions) == 1:
                if decompositions[0]["meta_morphemes"]:
                    postprocessed_data.append({
                        "root": root,
                        "pos": decompositions[0]["pos"],
                        "derivation": word,
                        "morphemes": decompositions[0]["morphemes"],
                        "meta_morphemes": decompositions[0]["meta_morphemes"]
                    })
                    continue
            
            best_decomposition = infer_best_decomposition_tr(word, decompositions, tr_dictionary)
        
            if best_decomposition:
                postprocessed_data.append({
                    "root": root,
                    "pos": best_decomposition["pos"],
                    "derivation": word,
                    "morphemes": best_decomposition["morphemes"],
                    "meta_morphemes": best_decomposition["meta_morphemes"]
                })
    
    return postprocessed_data

def preprocess_tr_btwd_data(datapath, num_samples=None):
    input_data = read_json(datapath)
    data = input_data["data"]

    if num_samples is not None:
        data = random.sample(data, num_samples)
    
    seen_words = set()
    preprocessed_data = defaultdict(dict)

    for sample in tqdm(data, total=len(data), desc="Preprocessing BTWD data for Morph tasks", leave=False, position=0):
        for sentence in tqdm(sample["sentences"], total=len(sample["sentences"]), desc="Processing sentences", leave=False, position=1):
            for word in sentence.split():
                word = word.strip().lower()

                if word in seen_words:
                    continue

                seen_words.add(word)
                decompositions = decompose_tr(word.strip())
                for decomposition in decompositions:
                    if decomposition.root not in preprocessed_data or word not in preprocessed_data[decomposition.root]:
                        preprocessed_data[decomposition.root][word] = []
                    preprocessed_data[decomposition.root][word].append(decomposition.to_json())

    return preprocessed_data

def preprocess_en_morpholex_data(datapath, num_samples=None):
    data = pd.read_excel(datapath, sheet_name=["0-1-1", "0-1-2", "0-1-3", "0-1-4", "0-2-1", "0-2-2", "0-2-3", "0-3-1"])
    data = pd.concat([data[sheet] for sheet in data.keys()])

    if num_samples is not None:
        data = data.sample(num_samples)

    words = []

    for i, row in data.iterrows():
        word = row["Word"]
        segmentation = row["MorphoLexSegm"]
        morphemes = re.findall(r"[A-Za-z]+", segmentation)
        if word == "".join(morphemes):
            words.append({
                "root": morphemes[0],
                "pos": row["POS"],
                "derivation": word,
                "morphemes": morphemes[1:],
                "meta_morphemes": None
            })

    return words

def prepare_comp_data(datapath, num_samples=None):
    input_data = read_json(datapath)
    data = input_data["data"]
    comp_map = {}

    if num_samples is not None:
        data = random.sample(data, num_samples)

    data = sorted(data, key=lambda x: len(x["meta_morphemes"]), reverse=True)

    for sample in tqdm(data, total=len(data), desc="Preparing TR compositional data for Morph tasks"):
        morphemes_key = frozenset(sample["meta_morphemes"])
        if morphemes_key not in comp_map:
            comp_map[morphemes_key] = []
        
        comp_map[morphemes_key].append(sample)
    
    return list(comp_map.values())

def prepare_tr_btwd_balanced_data(datapath, num_samples=50):
    input_data = read_json(datapath)
    data = input_data["data"]
    
    balanced_data = {i+1: [] for i in range(10)}

    seen_roots = {i+1: set() for i in range(10)}
    meta_suffix_comb_map = {i+1: set() for i in range(10)}
    balanced_data_extra = {i+1: [] for i in range(10)}
    balanced_data_root_extra = {i+1: [] for i in range(10)}
    
    # prioritize samples with unseen meta morphemes
    for sample in tqdm(data, total=len(data), desc="Preparing TR BTWD balanced data"):
        num_suffixes = len(sample["morphemes"])
        if num_suffixes > 0:
            if sample["root"] not in seen_roots[num_suffixes]:
                suffix_comb_set = meta_suffix_comb_map[num_suffixes]
                if len(suffix_comb_set) < num_samples:
                    if len(sample["root"]) > 3 and tuple(sample["meta_morphemes"]) not in suffix_comb_set:
                        balanced_data[num_suffixes].append(sample)
                        seen_roots[num_suffixes].add(sample["root"])
                        suffix_comb_set.add(tuple(sample["meta_morphemes"]))
                    else:
                        balanced_data_extra[num_suffixes].append(sample)
            else:
                balanced_data_root_extra[num_suffixes].append(sample)
    
    print([len(lst) for lst in balanced_data.values()])

    suffix_comb_map = {i+1: set() for i in range(10)}
    extra_morpheme_data = {i+1: [] for i in range(10)}
    
    # prioritize samples with unseen morphemes
    for num_suffixes, extra_samples in balanced_data_extra.items():
        while len(balanced_data[num_suffixes]) < num_samples and extra_samples:
            extra_sample = extra_samples.pop()
            suffix_comb_set = suffix_comb_map[num_suffixes]
            if tuple(sample["morphemes"]) not in suffix_comb_set:
                balanced_data[num_suffixes].append(extra_sample)
                suffix_comb_map[num_suffixes].add(tuple(sample["morphemes"]))
            else:
                extra_morpheme_data[num_suffixes].append(extra_sample)
    
    print([len(lst) for lst in balanced_data.values()])

    extra_seen_roots = {i+1: set() for i in range(10)}

    # prioritize samples with unseen roots
    for num_suffixes, extra_samples in extra_morpheme_data.items():
        while len(balanced_data[num_suffixes]) < num_samples and extra_samples:
            extra_sample = extra_samples.pop()
            if extra_sample["root"] not in extra_seen_roots[num_suffixes]:
                balanced_data[num_suffixes].append(extra_sample)
                extra_seen_roots[num_suffixes].add(extra_sample["root"])
    
    print([len(lst) for lst in balanced_data.values()])
    
    extra_seen_suffix_combs = {i+1: set() for i in range(10)}
    
    # add the rest
    for num_suffixes, extra_samples in balanced_data_root_extra.items():
        while len(balanced_data[num_suffixes]) < num_samples and extra_samples:
            extra_sample = extra_samples.pop()
            if tuple(extra_sample["morphemes"]) not in extra_seen_suffix_combs[num_suffixes]:
                balanced_data[num_suffixes].append(extra_sample)
                extra_seen_suffix_combs[num_suffixes].add(tuple(extra_sample["morphemes"]))
    
    print([len(lst) for lst in balanced_data.values()])
    
    return concatenate_lists(list([lst for lst in balanced_data.values() if len(lst) > int(num_samples/2)]))

def prepare_en_morpholex_balanced_data(datapath, num_samples=25):
    input_data = read_json(datapath)
    data = input_data["data"]
    seen_roots = set()
    suffix_comb_map = {i+1: set() for i in range(10)}
    balanced_data = {i+1: [] for i in range(10)}
    balanced_data_extra = {i+1: [] for i in range(10)}

    for sample in tqdm(data, total=len(data), desc="Preparing EN MorphoLex balanced data"):
        num_suffixes = len(sample["morphemes"])
        if sample["root"] not in seen_roots and num_suffixes > 0:
            suffix_comb_set = suffix_comb_map[num_suffixes]
            if len(suffix_comb_set) < num_samples:
                if tuple(sample["morphemes"]) not in suffix_comb_set:
                    balanced_data[num_suffixes].append(sample)
                    seen_roots.add(sample["root"])
                    suffix_comb_set.add(tuple(sample["morphemes"]))
                else:
                    balanced_data_extra[num_suffixes].append(sample)
    
    for num_suffixes, extra_samples in balanced_data_extra.items():
        if len(balanced_data[num_suffixes]) < num_samples:
            balanced_data[num_suffixes].extend(extra_samples[:num_samples-len(balanced_data[num_suffixes])])
    
    return concatenate_lists(list([lst for lst in balanced_data.values() if len(lst) > int(num_samples/2)]))

def preprocess_tr_sense_data(datapath, num_samples=None):
    data = read_json(datapath)
    prep_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preprocessing TR sense data"):
        words = sample["word"].split()
        
        if len(words) == 1:
            word = words[0].strip().lower()
            decompositions = [decomp.to_json() for decomp in decompose_tr(word)]
            decompositions = infer_best_decomposition_tr(word, decompositions)
            if decompositions:
                prep_data.append({
                    "id": f"tr-sense-{i}",
                    "root": decompositions[0]["root"],
                    "pos": decompositions[0]["pos"],
                    "derivation": word,
                    "morphemes": decompositions[0]["morphemes"],
                    "meta_morphemes": decompositions[0]["meta_morphemes"],
                    "meanings": sample["meanings"]
                })
    
    return prep_data

def prepare_tr_sense_balanced_data(datapath, num_samples=50):
    input_data = read_json(datapath)
    data = random.sample(input_data["data"], len(input_data["data"]))
    seen_roots = set()
    suffix_comb_map = {i+1: set() for i in range(10)}
    balanced_data = {i+1: [] for i in range(10)}
    balanced_data_extra = {i+1: [] for i in range(10)}

    for sample in tqdm(data, total=len(data), desc="Preparing TR sense balanced data"):
        num_suffixes = len(sample["morphemes"])
        if sample["root"] not in seen_roots and num_suffixes > 0:
            suffix_comb_set = suffix_comb_map[num_suffixes]
            if len(suffix_comb_set) < num_samples:
                if len(sample["root"]) > 3 and tuple(sample["morphemes"]) not in suffix_comb_set and (len(sample["morphemes"]) > 1 or len(sample["morphemes"][0]) > 1):
                    balanced_data[num_suffixes].append(sample)
                    seen_roots.add(sample["root"])
                    suffix_comb_set.add(tuple(sample["morphemes"]))
                else:
                    balanced_data_extra[num_suffixes].append(sample)
    
    for num_suffixes, extra_samples in balanced_data_extra.items():
        if len(balanced_data[num_suffixes]) < num_samples:
            balanced_data[num_suffixes].extend(extra_samples[:num_samples-len(balanced_data[num_suffixes])])
    
    return concatenate_lists(list([lst for lst in balanced_data.values() if len(lst) > int(num_samples/2)]))

DATA_PROCESSOR_MAP = {
    "tr_btwd_json": (prepare_tr_btwd_json_data, ""), 
    "tr_btwd_prep": (preprocess_tr_btwd_data, "_prep"),
    "tr_btwd_post": (postprocess_tr_btwd_data, "_post"),
    "en_morpholex_prep": (preprocess_en_morpholex_data, "_prep"),
    "tr_comp_prep": (prepare_comp_data, "_comp"),
    "tr_btwd_balanced": (prepare_tr_btwd_balanced_data, "_balanced"),
    "en_morpholex_balanced": (prepare_en_morpholex_balanced_data, "_balanced"),
    "tr_sense_prep": (preprocess_tr_sense_data, "_prep"),
    "tr_sense_balanced": (prepare_tr_sense_balanced_data, "_balanced")
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to raw data", required=True)
    parser.add_argument("-l", "--language", type=str, help="Language", choices=LANGUAGES, default="tr")
    parser.add_argument("-p", "--processor", type=str, default="tr_btwd_prep", help="Data processor name")
    parser.add_argument("-n", "--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")

    args = parser.parse_args()

    preprocessed_data = DATA_PROCESSOR_MAP[args.processor][0](args.datapath, args.num_samples)

    datapath = pathlib.Path(args.datapath)
    output_dir = pathlib.Path(args.output_dir) if args.output_dir is not None else datapath.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    preprocessed_data_path_stem = output_dir / f"{datapath.stem}{DATA_PROCESSOR_MAP[args.processor][1]}{args.suffix}"

    output_data = {
        "metadata": {
            "source": args.datapath,
            "processor": args.processor,
            "language": args.language,
            "size": len(preprocessed_data)
        },
        "data": preprocessed_data
    }
    write_json(output_data, preprocessed_data_path_stem.with_suffix(".json"), ensure_ascii=False)

if __name__ == "__main__":
    main()