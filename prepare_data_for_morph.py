import sys
import argparse
import pathlib
from tqdm import tqdm
import pandas as pd
import random
import numpy as np
from itertools import permutations
from collections import defaultdict

from utils import read_json, write_json
from morphology import decompose_tr

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

def prepare_btwd_for_morph(datapath, num_samples=None):
    data = read_json(datapath)

    if num_samples is not None:
        data = random.sample(data, num_samples)
    
    seen_words = set()
    morph_data = defaultdict(dict)

    for sample in tqdm(data, total=len(data), desc="Preparing BTWD data for Morph tasks", leave=False, position=0):
        for sentence in tqdm(sample["sentences"], total=len(sample["sentences"]), desc="Processing sentences", leave=False, position=1):
            for word in sentence.split():
                word = word.strip()

                if word in seen_words:
                    continue

                seen_words.add(word)
                decompositions = decompose_tr(word.strip())
                for decomposition in decompositions:
                    if decomposition.root not in morph_data or word not in morph_data[decomposition.root]:
                        morph_data[decomposition.root][word] = []
                    morph_data[decomposition.root][word].append(decomposition.to_json())

    return morph_data

DATASET_PROCESSOR_MAP = {
    "pilot": prepare_pilot_data_for_morph,
    "btwd": prepare_btwd_for_morph
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("--dataset", type=str, default="pilot", help="Dataset name")
    parser.add_argument("--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("--suffix", type=str, default="", help="Custom suffix for output file path.")

    args = parser.parse_args()

    morph_data = DATASET_PROCESSOR_MAP[args.dataset](args.datapath, args.num_samples)

    datapath = pathlib.Path(args.datapath)
    morph_data_path_stem = datapath.parent / f"{datapath.stem}_prep{args.suffix}"

    write_json(morph_data, morph_data_path_stem.with_suffix(".json"), ensure_ascii=False)
    # pd.DataFrame(morph_data).to_csv(morph_data_path_stem.with_suffix(".csv"), index=False)

if __name__ == "__main__":
    main()