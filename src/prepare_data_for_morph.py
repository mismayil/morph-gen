import sys
import argparse
import pathlib
from tqdm import tqdm
import random
from itertools import permutations
import json

from utils import read_json, write_json
from morphology import generate_nonce_word_tr

TR_DICTIONARY_PATH = "../../data/tr/gts.json"

def _read_tr_dictionary():
    dictionary = []
    with open(TR_DICTIONARY_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            json_line = json.loads(line)
            dictionary.append(json_line["madde"])
    return dictionary

def prepare_tr_pilot_data_for_morph(input_data, num_samples=None):
    data = input_data["data"]

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

def prepare_tr_data_for_morph(input_data, num_samples=None):
    data = input_data["data"]
    
    morph_data = []

    for sample in tqdm(data, desc="Preparing data for Morph tasks"):
        suffixes = sample["morphemes"]

        if len(suffixes) > 1:
            suffix_perms = list(permutations(suffixes))
            options = set()

            for suffix_perm in suffix_perms:
                derivation = sample["root"] + ''.join(suffix_perm)

                if derivation != sample["derivation"]:
                    options.add(derivation)

            options = random.sample(list(options), min(len(options), 5))

            morph_data.append({
                "root": sample["root"],
                "pos": sample["pos"],
                "suffixes": suffixes,
                "derivation": sample["derivation"],
                "options": [sample["derivation"]] + list(options),
                "answer": 0
            })
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_tr_nonce_data_for_morph(input_data, num_samples=None):
    dictionary = _read_tr_dictionary()
    data = input_data["data"]
    nonce_data = []

    for sample in tqdm(data, total=len(data), desc="Preparing nonce data for Morph tasks"):
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
    "tr_pilot_morph": (prepare_tr_pilot_data_for_morph, "_morph"),
    "tr_morph": (prepare_tr_data_for_morph, "_morph"),
    "tr_morph_nonce": (prepare_tr_nonce_data_for_morph, "_nonce")
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to data", required=True)
    parser.add_argument("-p", "--processor", type=str, default="pilot_morph", help="Data processor name")
    parser.add_argument("-n", "--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")

    args = parser.parse_args()
    input_data = read_json(args.datapath)
    morph_data = DATA_PROCESSOR_MAP[args.processor][0](args.datapath, args.num_samples)

    datapath = pathlib.Path(args.datapath)
    output_dir = pathlib.Path(args.output_dir) if args.output_dir is not None else datapath.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    morph_data_path_stem = output_dir / f"{datapath.stem}{DATA_PROCESSOR_MAP[args.processor][1]}{args.suffix}"

    output_data = {
        "metadata": {
            "source": args.datapath,
            "processor": args.processor,
            "language": input_data["metadata"]["language"]
        },
        "data": morph_data
    }

    write_json(output_data, morph_data_path_stem.with_suffix(".json"), ensure_ascii=False)

if __name__ == "__main__":
    main()