import sys
import argparse
import pathlib
from tqdm import tqdm
import pandas as pd
import random
import numpy as np
from itertools import permutations
from collections import defaultdict
import re, json

from utils import read_json, write_json
from morphology import decompose_tr, generate_nonce_word_tr

TURKISH_DICTIONARY_PATH = "../data/gts.json"

def _read_turkish_dictionary():
    dictionary = []
    with open(TURKISH_DICTIONARY_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            json_line = json.loads(line)
            dictionary.append(json_line["madde"])
    return dictionary

def prepare_pilot_data_for_morph(datapath, num_samples=None):
    data = read_json(datapath)

    if num_samples is not None:
        data = random.sample(data, num_samples)
    
    morph_data = []

    for sample in tqdm(data, desc="Preparing pilot data for Morph tasks"):
        root = sample["root"]
        alt_root = sample["alt_root"]
        suffixes = sample["suffixes"]
        derivation = sample["derivation"]
        alt_derivation = sample["derivation"].replace(root, alt_root)

        suffix_perms = list(permutations(suffixes))
        root_options = set()
        alt_root_options = set()

        for suffix_perm in suffix_perms:
            root_derivation = root + ''.join(suffix_perm)
            alt_root_derivation = alt_root + ''.join(suffix_perm)

            if root_derivation != derivation:
                root_options.add(root_derivation)
            
            if alt_root_derivation != alt_derivation:
                alt_root_options.add(alt_root_derivation)

        root_options = random.sample(list(root_options), min(len(root_options), 5))
        alt_root_options = random.sample(list(alt_root_options), min(len(alt_root_options), 5))

        morph_data.append({
            "root": root,
            "pos": sample["pos"],
            "suffixes": suffixes,
            "derivation": derivation,
            "options": [derivation] + list(root_options),
            "answer": 0
        })

        morph_data.append({
            "root": alt_root,
            "pos": sample["pos"],
            "suffixes": suffixes,
            "derivation": alt_derivation,
            "options": [alt_derivation] + list(alt_root_options),
            "answer": 0
        })
    
    return morph_data

def prepare_btwd_json_data(datapath, num_samples=None):
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

def postprocess_btwd_data(datapath, num_samples=None):
    def _is_noun_pronoun(pos):
        return pos in ["NN", "NNP", "ADD", "VN", "PRD", "PRF", "PRI", "PRP", "PRP$", "PRR", "WP"]

    data = read_json(datapath)

    if num_samples is not None:
        data = dict(random.sample(list(data.items()), num_samples))

    resolved_data = defaultdict(dict)

    for root, word_map in tqdm(data.items(), total=len(data.items()), desc="Post-processing btwd data"):
        new_word_map = {}

        for word, decompositions in word_map.items():
            if "'" in word:
                continue

            if len(decompositions) == 1:
                if decompositions[0]["meta_morphemes"]:
                    new_word_map[word] = [decompositions[0]]
                    continue
            
            valid_decompositions = []

            for decomposition in decompositions:
                if not decomposition["meta_morphemes"]:
                    continue
                
                morpheme_tuples = [(decomposition["meta_morphemes"][i], decomposition["meta_morphemes"][i+1]) for i in range(len(decomposition["meta_morphemes"])-1)]
                morpheme_triples = [(decomposition["meta_morphemes"][i], decomposition["meta_morphemes"][i+1], decomposition["meta_morphemes"][i+2]) for i in range(len(decomposition["meta_morphemes"])-2)]

                if "s" in decomposition["morphemes"]:
                    s_index = decomposition["morphemes"].index("s")
                    meta_s = decomposition["meta_morphemes"][s_index]
                    if meta_s == "sH" or meta_s == "SH":
                        continue
                
                if "lArH" in decomposition["meta_morphemes"]:
                    continue
                
                if ("lAr", "Hm", "YHz") in morpheme_triples or ("lAr", "Hn", "YHz") in morpheme_triples:
                    alt_la = any([("HmHz" in decomp["meta_morphemes"] or "HnHz" in decomp["meta_morphemes"]) for decomp in decompositions])
                    if alt_la:
                        continue

                if ("lA", "Hr") in morpheme_tuples or ("lA", "Hn") in morpheme_tuples or ("lA", "Hş") in morpheme_tuples:
                    alt_la = any([("lAr" in decomp["meta_morphemes"] or "lAn" in decomp["meta_morphemes"] or "lAş" in decomp["meta_morphemes"]) for decomp in decompositions])
                    if alt_la:
                        continue
                
                valid_decompositions.append(decomposition)
            
            if valid_decompositions:
                new_word_map[word] = valid_decompositions
        
        if new_word_map:
            resolved_data[root] = new_word_map
    
    return resolved_data

def preprocess_btwd_data(datapath, num_samples=None):
    data = read_json(datapath)

    if num_samples is not None:
        data = random.sample(data, num_samples)
    
    seen_words = set()
    morph_data = defaultdict(dict)

    for sample in tqdm(data, total=len(data), desc="Preparing BTWD data for Morph tasks", leave=False, position=0):
        for sentence in tqdm(sample["sentences"], total=len(sample["sentences"]), desc="Processing sentences", leave=False, position=1):
            for word in sentence.split():
                word = word.strip().lower()

                if word in seen_words:
                    continue

                seen_words.add(word)
                decompositions = decompose_tr(word.strip())
                for decomposition in decompositions:
                    if decomposition.root not in morph_data or word not in morph_data[decomposition.root]:
                        morph_data[decomposition.root][word] = []
                    morph_data[decomposition.root][word].append(decomposition.to_json())

    return morph_data

def prepare_btwd_for_morph(datapath, num_samples=None):
    data = read_json(datapath)
    
    morph_data = []

    for root, word_map in tqdm(data.items(), desc="Preparing BTWD data for Morph tasks"):
        for word, decompositions in word_map.items():
            decomposition = decompositions[0]
            suffixes = decomposition["morphemes"]

            if len(suffixes) > 1:
                suffix_perms = list(permutations(suffixes))
                options = set()

                for suffix_perm in suffix_perms:
                    derivation = root + ''.join(suffix_perm)

                    if derivation != word:
                        options.add(derivation)

                options = random.sample(list(options), min(len(options), 5))

                morph_data.append({
                    "root": root,
                    "pos": decomposition["pos"],
                    "suffixes": suffixes,
                    "derivation": word,
                    "options": [word] + list(options),
                    "answer": 0
                })
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_btwd_nonce_data(datapath, num_samples=None):
    dictionary = _read_turkish_dictionary()
    data = read_json(datapath)
    nonce_data = []

    for sample in tqdm(data, total=len(data), desc="Preparing BTWD nonce data for Morph tasks"):
        root = sample["root"]
        pos = sample["pos"]
        suffixes = sample["suffixes"]
        derivation = sample["derivation"]
        options = sample["options"]

        while True:
            nonce_word = generate_nonce_word_tr(root)
            if nonce_word not in dictionary:
                break

        nonce_data.append({
            "original_root": root,
            "root": nonce_word,
            "pos": pos,
            "suffixes": suffixes,
            "derivation": derivation.replace(root, nonce_word, 1),
            "options": [option.replace(root, nonce_word, 1) for option in options],
            "answer": 0
        })
    
    if num_samples is not None:
        nonce_data = random.sample(nonce_data, num_samples)
    
    return nonce_data

DATA_PROCESSOR_MAP = {
    "pilot_morph": (prepare_pilot_data_for_morph, "_morph"),
    "btwd_json": (prepare_btwd_json_data, ""), 
    "btwd_prep": (preprocess_btwd_data, "_prep"),
    "btwd_post": (postprocess_btwd_data, "_post"),
    "btwd_morph": (prepare_btwd_for_morph, "_morph"),
    "btwd_nonce": (prepare_btwd_nonce_data, "_nonce")
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to data", required=True)
    parser.add_argument("-p", "--processor", type=str, default="pilot_morph", help="Data processor name")
    parser.add_argument("-n", "--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")

    args = parser.parse_args()

    morph_data = DATA_PROCESSOR_MAP[args.processor][0](args.datapath, args.num_samples)

    datapath = pathlib.Path(args.datapath)
    morph_data_path_stem = datapath.parent / f"{datapath.stem}{DATA_PROCESSOR_MAP[args.processor][1]}{args.suffix}"

    write_json(morph_data, morph_data_path_stem.with_suffix(".json"), ensure_ascii=False)
    # pd.DataFrame(morph_data).to_csv(morph_data_path_stem.with_suffix(".csv"), index=False)

if __name__ == "__main__":
    main()