import sys
import argparse
import pathlib
from tqdm import tqdm
import random
from itertools import permutations
import json

from utils import read_json, write_json
from morphology import generate_nonce_word_tr, generate_nonce_word_en, segment_by_tokenizer, read_en_dictionary, read_tr_dictionary

def prepare_sample_for_tasks(sample, separator=""):
    suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
    ref_derivation = sample["root"] + separator + separator.join(suffixes)

    if len(suffixes) > 0:
        suffix_perms = list(permutations(suffixes))
        options = set()

        for suffix_perm in suffix_perms:
            derivation = sample["root"] + separator + separator.join(suffix_perm)

            if derivation != ref_derivation:
                options.add(derivation)

        options = random.sample(list(options), min(len(options), 5))
        sentence = sample.get("sentence")

        return {
            "original_root": sample["original_root"] if "original_root" in sample else None,
            "root": sample["root"],
            "pos": sample["pos"],
            "suffixes": suffixes,
            "derivation": ref_derivation,
            "options": [ref_derivation] + list(options),
            "answer": 0,
            "meta_suffixes": sample.get("meta_morphemes"),
            "sentence": sentence.lower().replace(ref_derivation, "___") if sentence else None,
            "meaning": sample.get("meaning"),
        }
    
    return None

def prepare_tr_data_for_tasks(input_data, num_samples=None, separator="", *args, **kwargs):
    data = input_data["data"]
    
    morph_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing data TR for Morph tasks"):
        morph_sample = prepare_sample_for_tasks(sample, separator)
        if morph_sample is not None:
            morph_data.append({"id": f"tr-btwd-id-{i}", **morph_sample})
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_tr_nonce_data_for_tasks(input_data, num_samples=None, *args, **kwargs):
    dictionary = read_tr_dictionary()
    data = input_data["data"]
    nonce_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing TR nonce data for Morph tasks"):
        root = sample["root"]
        pos = sample["pos"]
        suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
        derivation = sample["derivation"]
        options = sample["options"]

        while True:
            nonce_word = generate_nonce_word_tr(root)
            if nonce_word not in dictionary:
                break
        
        nonce_derivation = derivation.replace(root, nonce_word, 1)

        nonce_data.append({
            "id": f"tr-btwd-ood-{i}",
            "original_root": root,
            "original_derivation": derivation,
            "root": nonce_word,
            "pos": pos,
            "suffixes": suffixes,
            "derivation": nonce_derivation,
            "options": [option.replace(root, nonce_word, 1) for option in options],
            "answer": 0,
            "similar": sample.get("similar"),
            "meta_suffixes": sample.get("meta_morphemes") if "meta_morphemes" in sample else sample.get("meta_suffixes"),
            "sentence": sample.get("sentence"),
            "meaning": sample.get("meaning")
        })
    
    if num_samples is not None:
        nonce_data = random.sample(nonce_data, num_samples)
    
    return nonce_data

def prepare_en_data_for_tasks(input_data, num_samples=None, separator="", *args, **kwargs):
    data = input_data["data"]
    
    morph_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing EN data for Morph tasks"):
        morph_sample = prepare_sample_for_tasks(sample, separator)
        if morph_sample is not None:
            morph_data.append({"id": f"en-morpholex-id-{i}", **morph_sample})
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_en_nonce_data_for_tasks(input_data, num_samples=None, *args, **kwargs):
    dictionary = read_en_dictionary()
    data = input_data["data"]
    nonce_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing EN nonce data for Morph tasks"):
        root = sample["root"]
        pos = sample["pos"]
        suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
        derivation = sample["derivation"]
        options = sample["options"]

        while True:
            nonce_word = generate_nonce_word_en(root)
            if nonce_word not in dictionary:
                break
        
        nonce_derivation = derivation.replace(root, nonce_word, 1)
    
        nonce_data.append({
            "id": f"en-morpholex-ood-{i}",
            "original_root": root,
            "original_derivation": derivation,
            "root": nonce_word,
            "pos": pos,
            "suffixes": suffixes,
            "derivation": nonce_derivation,
            "options": [option.replace(root, nonce_word, 1) for option in options],
            "answer": 0,
            "meta_suffixes": sample.get("meta_morphemes") if "meta_morphemes" in sample else sample.get("meta_suffixes"),
            "sentence": sample.get("sentence"),
            "meaning": sample.get("meaning"),
        })
    
    if num_samples is not None:
        nonce_data = random.sample(nonce_data, num_samples)
    
    return nonce_data

def prepare_tr_comp_data_for_tasks(input_data, num_samples=None, separator="", *args, **kwargs):
    data = input_data["data"]
    
    morph_data = []

    for i, samples in tqdm(enumerate(data), desc="Preparing comp data TR for Morph tasks"):
        if len(samples) > 1:
            ref_sample = samples[0]
            similar_samples = []
            seen_suffixes = [tuple(ref_sample["morphemes"])]

            for subsample in samples[1:]:
                if tuple(subsample["morphemes"]) not in seen_suffixes:
                    morph_sample = prepare_sample_for_tasks(subsample, separator)
                    if morph_sample is not None:
                        similar_samples.append(morph_sample)
                        seen_suffixes.append(tuple(subsample["morphemes"]))
            
            if len(similar_samples) > 0:
                morph_data.append({
                    "id": f"tr-comp-{i}",
                    **prepare_sample_for_tasks(ref_sample, separator),
                    "similar": similar_samples
                })
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_tok_aligned_data_for_tasks(input_data, num_samples=None, separator="", model="gpt-4", *args, **kwargs):
    data = input_data["data"]
    tok_aligned_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing tokenization aligned data for tasks"):
        ref_derivation = sample["derivation"]
        tokens = segment_by_tokenizer(ref_derivation, model, sample["root"])
        root_token = tokens[0]
        token_perms = permutations(tokens[1:])
        options = set()

        for token_perm in token_perms:
            derivation = root_token + separator + separator.join(token_perm)

            if derivation != ref_derivation:
                options.add(derivation)
            
            if len(options) >= 5:
                break

        options = random.sample(list(options), len(options))
        tok_aligned_data.append({
            **sample,
            "ref_root": sample["root"],
            "ref_suffixes": sample["suffixes"],
            "ref_meta_suffixes": sample.get("meta_morphemes"),
            "root": root_token,
            "suffixes": tokens[1:],
            "options": [ref_derivation] + list(options),
            "answer": 0
        })
    
    if num_samples is not None:
        tok_aligned_data = random.sample(tok_aligned_data, num_samples)

    return tok_aligned_data

def prepare_tr_sense_data_for_tasks(input_data, num_samples=None, separator="", *args, **kwargs):
    data = input_data["data"]
    
    morph_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing data TR for Morph tasks"):
        morph_sample = prepare_sample_for_tasks(sample, separator)
        if morph_sample is not None:
            meanings = [m for m in sample["meanings"] if len(m.split()) > 1]
            if meanings:
                morph_data.append({"id": sample.get("id", f"tr-sense-{i}"), **morph_sample, "meaning": sample["meanings"][0]})
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

DATA_PROCESSOR_MAP = {
    "tr_morph": (prepare_tr_data_for_tasks, "_morph"),
    "tr_morph_nonce": (prepare_tr_nonce_data_for_tasks, "_nonce"),
    "en_morph": (prepare_en_data_for_tasks, "_morph"),
    "en_morph_nonce": (prepare_en_nonce_data_for_tasks, "_nonce"),
    "tr_comp_morph": (prepare_tr_comp_data_for_tasks, "_morph"),
    "tok_aligned": (prepare_tok_aligned_data_for_tasks, "_tok_aligned"),
    "tr_sense": (prepare_tr_sense_data_for_tasks, "_sense")
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to data", required=True)
    parser.add_argument("-p", "--processor", type=str, default="pilot_morph", help="Data processor name")
    parser.add_argument("-n", "--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")
    parser.add_argument("-t", "--separator", type=str, default="", help="Separator to use between morphemes. Defaults to empty string.")

    args = parser.parse_args()
    input_data = read_json(args.datapath)
    morph_data = DATA_PROCESSOR_MAP[args.processor][0](input_data, args.num_samples, separator=args.separator)

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