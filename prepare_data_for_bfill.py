import sys
import argparse
import pathlib
from tqdm import tqdm
import pandas as pd
import random
import numpy as np
from itertools import product

from utils import read_json, write_json, get_morphemes_from_sentence, TURKISH_MORPH_MAP

def prepare_bilkent_data_for_bfill(datapath, num_samples=None):
    data = read_json(datapath)

    if num_samples is not None:
        data = random.sample(data, num_samples)
    
    bfill_data = []

    for sample in tqdm(data, desc="Preparing Bilkent data for BFill"):
        sentences = random.sample(sample["sentences"][1:-1], 1)
        sentence = sentences[0]
        morpheme_sets = get_morphemes_from_sentence(sentence)
        morpheme_set_lens = [len(morpheme_set["morphemes"]) for morpheme_set in morpheme_sets]
        longest_morpheme_set = morpheme_sets[np.argmax(morpheme_set_lens)]

        suffixes = []

        for morpheme in longest_morpheme_set["morphemes"][1:]:
            suffix_sets = []
            for char in morpheme:
                suffix_set = TURKISH_MORPH_MAP.get(char, [char.lower()])
                suffix_sets.append(suffix_set)
            suffixes.extend(["".join(suffix_chars) for suffix_chars in list(product(*suffix_sets))])

        bfill_data.append({
            "id": sample["id"],
            "full_sentence": sentence,
            "sentence": sentence.replace(longest_morpheme_set["word"], "___"),
            "words": [longest_morpheme_set["morphemes"][0]],
            "suffixes": np.random.permutation(suffixes).tolist(),
            "missing_words": [longest_morpheme_set["word"]],
            "morphemes": [longest_morpheme_set["morphemes"]],
        })
    
    return bfill_data

DATASET_PROCESSOR_MAP = {
    "bilkent": prepare_bilkent_data_for_bfill
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("--dataset", type=str, default="bilkent", help="Dataset name")
    parser.add_argument("--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("--suffix", type=str, default="", help="Custom suffix for output file path.")

    args = parser.parse_args()

    bfill_data = DATASET_PROCESSOR_MAP[args.dataset](args.datapath, args.num_samples)

    datapath = pathlib.Path(args.datapath)
    bfill_data_path_stem = datapath.parent / f"{datapath.stem}_bfill{args.suffix}"

    write_json(bfill_data, bfill_data_path_stem.with_suffix(".json"), ensure_ascii=False)
    pd.DataFrame(bfill_data).to_csv(bfill_data_path_stem.with_suffix(".csv"), index=False)

if __name__ == "__main__":
    main()