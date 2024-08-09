import argparse
import pathlib
import random
from itertools import permutations, product

from tqdm import tqdm
import random
from itertools import permutations
import re

from utils import read_json, write_json, levenshtein_distance
from morphology import generate_nonce_word_tr, generate_nonce_word_en, segment_by_tokenizer, read_en_dictionary, generate_nonce_word_fi

NONCE_GENERATOR = {
    "tr": generate_nonce_word_tr,
    "en": generate_nonce_word_en,
    "fi": generate_nonce_word_fi
}

def check_if_has_double_vowel(word):
    vowels = ["a", "ı", "o", "u", "e", "i", "ö", "ü"]
    vowels_str = ''.join(vowels)
    vowel_re = re.compile(f"[{vowels_str}][{vowels_str}]")
    return re.search(vowel_re, word)

def select_negative_options(negative_options, ref_option, root, strategy="lev", num_options=4):
    if strategy == "lev":
        return sorted(
            list(negative_options), key=lambda x: levenshtein_distance(x, ref_option)
        )[:num_options]
    elif strategy == "random":
        return random.sample(list(negative_options), min(len(negative_options), num_options))
    elif strategy == "no_double_vowel":
        double_vowel_options = []
        no_double_vowel_options = []
        for option in negative_options:
            # assume no prefixes
            suffix = option.replace(root, "", 1)
            if check_if_has_double_vowel(suffix):
                double_vowel_options.append(option)
            else:
                no_double_vowel_options.append(option)
        
        # prefer no double vowel options
        options = sorted(
            list(no_double_vowel_options), key=lambda x: levenshtein_distance(x, ref_option)
        )[:num_options]

        # fill the rest with double vowel options
        if len(options) < num_options:
            double_vowel_options = sorted(list(double_vowel_options), key=lambda x: levenshtein_distance(x, ref_option))
            options += double_vowel_options[:num_options - len(options)]
        
        return options
    else:
        raise ValueError(f"Invalid strategy: {strategy}")

def get_negative_options(root, prefixes, suffixes, ref_derivation, negative_prefixes=None, negative_suffixes=None, separator=""):
    prefix_perms = []
    suffix_perms = []
    affix_perms = []

    if prefixes:
        prefix_perms = list(permutations(prefixes))
    
    if suffixes:
        suffix_perms = list(permutations(suffixes))
    
    if suffix_perms and prefix_perms:
        affix_perms = product(prefix_perms, suffix_perms)
    elif suffix_perms:
        affix_perms = [((), suffix_perm) for suffix_perm in suffix_perms]
    elif prefix_perms:
        affix_perms = [(prefix_perm, ()) for prefix_perm in prefix_perms]

    negative_options = set()

    if affix_perms:
        for prefix_perm, suffix_perm in affix_perms:
            derivation = separator.join(prefix_perm) + separator + root + separator + separator.join(suffix_perm)

            if derivation != ref_derivation:
                negative_options.add(derivation)

    if not negative_options:
        if negative_prefixes:
            derivation = separator.join(negative_prefixes) + separator + root
            if derivation != ref_derivation:
                negative_options.add(derivation)
        
        if negative_suffixes:
            derivation = root + separator + separator.join(negative_suffixes)
            if derivation != ref_derivation:
                negative_options.add(derivation)
            
    return negative_options

def prepare_sample_for_tasks(sample, separator="", language="tr", verbose=False, no_nonce=False, option_strategy="lev", num_options=4):
    dictionary = read_en_dictionary()
    prefixes = sample.get("prefixes", [])
    suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
    negative_prefixes = sample.get("negative_prefixes", []) or []
    negative_suffixes = sample.get("negative_suffixes", []) or []
    ref_derivation = sample["derivation"]

    negative_options = get_negative_options(sample["root"], prefixes, suffixes, ref_derivation, 
                                            negative_prefixes=negative_prefixes, negative_suffixes=negative_suffixes,
                                            separator=separator)

    negative_options = select_negative_options(negative_options, ref_derivation, sample["root"], strategy=option_strategy, num_options=num_options)
    sentence = sample.get("sentence")

    attempt = 0
    nonce_word = None

    if not no_nonce:
        while True:
            if verbose:
                print(f"Generating nonce word for {sample['root']}")
            
            nonce_generator = NONCE_GENERATOR[language]
            nonce_word = nonce_generator(sample["root"])
            if nonce_word not in dictionary:
                break
            attempt += 1
            
            if verbose:
                print(f"Attempt {attempt} failed. Trying again.")

    return {
        "id": sample["id"],
        "id_root": sample["root"],
        "ood_root": nonce_word,
        "root": sample["root"],
        "pos": sample.get("pos"),
        "prefixes": prefixes,
        "suffixes": suffixes,
        "derivation": ref_derivation,
        "positive_options": [ref_derivation],
        "negative_options": list(negative_options),
        "meta_suffixes": sample.get("meta_morphemes"),
        "sentence": sentence.lower().replace(ref_derivation, "___") if sentence else None,
        "meaning": sample.get("meaning"),
    }


def prepare_data_for_tasks(
    input_data,
    num_samples=None,
    separator="",
    verbose=False,
    no_nonce=False,
    option_strategy="lev",
    num_options=4,
    *args,
    **kwargs,
):
    data = input_data["data"]
    language = input_data["metadata"]["language"]

    morph_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing data for Morph tasks"):
        morph_sample = prepare_sample_for_tasks(sample, separator, language=language, verbose=verbose, no_nonce=no_nonce, option_strategy=option_strategy, num_options=num_options)
        if morph_sample is not None:
            morph_data.append(morph_sample)
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

def prepare_nonce_data_for_tasks(input_data, num_samples=None, *args, **kwargs):
    data = input_data["data"]
    nonce_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing nonce data for Morph tasks"):
        id_root = sample["id_root"]
        id_derivation = sample["derivation"]
        positive_options = sample["positive_options"]
        negative_options = sample["negative_options"]
        ood_root = sample["ood_root"]

        nonce_derivation = id_derivation.replace(id_root, ood_root, 1)

        nonce_data.append({
            **sample,
            "id": f"{sample['id']}-ood",
            "id_root": sample["id_root"],
            "id_derivation": id_derivation,
            "ood_root": ood_root,
            "root": ood_root,
            "derivation": nonce_derivation,
            "positive_options": [option.replace(id_root, ood_root, 1) for option in positive_options],
            "negative_options": [option.replace(id_root, ood_root, 1) for option in negative_options],
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

def prepare_tok_aligned_data_for_tasks(input_data, num_samples=None, separator="", model="gpt-4", option_strategy="lev", num_options=4, *args, **kwargs):
    data = input_data["data"]
    tok_aligned_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing tokenization aligned data for tasks"):
        ref_derivation = sample["derivation"]
        negative_prefixes = sample.get("negative_prefixes", []) or []
        negative_suffixes = sample.get("negative_suffixes", []) or []
        tokens = segment_by_tokenizer(ref_derivation, model, sample["root"])
        root_token = tokens[0]
        suffixes = tokens[1:]

        if suffixes:
            negative_options = get_negative_options(root_token, [], suffixes, ref_derivation, 
                                                    negative_prefixes=negative_prefixes, negative_suffixes=negative_suffixes,
                                                    separator=separator)

            negative_options = select_negative_options(negative_options, ref_derivation, root_token, strategy=option_strategy, num_options=num_options)
            tok_aligned_data.append({
                **sample,
                "ref_root": sample["root"],
                "ref_suffixes": sample["suffixes"] if "suffixes" in sample else sample.get("morphemes"),
                "root": root_token,
                "suffixes": suffixes,
                "negative_options": list(negative_options)
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

def update_neg_sample_for_tasks(sample, separator="", language="tr", option_strategy="no_double_vowel", num_options=4, *args, **kwargs):
    prefixes = sample.get("prefixes", [])
    suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
    ref_derivation = sample["derivation"]
    negative_prefixes = sample.get("negative_prefixes", []) or []
    negative_suffixes = sample.get("negative_suffixes", []) or []

    negative_options = get_negative_options(sample["root"], prefixes, suffixes, ref_derivation, 
                                            negative_prefixes=negative_prefixes, negative_suffixes=negative_suffixes,
                                            separator=separator)

    negative_options = select_negative_options(negative_options, ref_derivation, sample["root"], strategy=option_strategy, num_options=num_options)

    return {
        **sample,
        "negative_options": list(negative_options)
    }

def update_neg_data_for_tasks(
    input_data,
    num_samples=None,
    separator="",
    option_strategy="no_double_vowel",
    num_options=4,
    *args,
    **kwargs,
):
    data = input_data["data"]
    language = input_data["metadata"]["language"]

    morph_data = []

    for i, sample in tqdm(enumerate(data), total=len(data), desc="Preparing data for Morph tasks"):
        morph_sample = update_neg_sample_for_tasks(sample, separator, language=language, option_strategy=option_strategy, num_options=num_options)
        if morph_sample is not None:
            morph_data.append(morph_sample)
    
    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data

DATA_PROCESSOR_MAP = {
    "morph": (prepare_data_for_tasks, "_morph"),
    "morph_nonce": (prepare_nonce_data_for_tasks, "_nonce"),
    "tr_comp_morph": (prepare_tr_comp_data_for_tasks, "_morph"),
    "tok_aligned": (prepare_tok_aligned_data_for_tasks, "_tok_aligned"),
    "tr_sense": (prepare_tr_sense_data_for_tasks, "_sense"),
    "update_neg_data": (update_neg_data_for_tasks, "_updated_neg"),
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to data", required=True)
    parser.add_argument("-p", "--processor", type=str, default="pilot_morph", help="Data processor name")
    parser.add_argument("-n", "--num-samples", type=int, default=None, help="Number of samples to process")
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")
    parser.add_argument("-t", "--separator", type=str, default="", help="Separator to use between morphemes. Defaults to empty string.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("-nn", "--no-nonce", action="store_true", help="Do not generate nonce words")
    parser.add_argument("-os", "--option-strategy", type=str, default="lev", help="Strategy to select negative options")
    parser.add_argument("-no", "--num-options", type=int, default=4, help="Number of negative options to select")

    args = parser.parse_args()
    input_data = read_json(args.datapath)
    morph_data = DATA_PROCESSOR_MAP[args.processor][0](input_data, args.num_samples, separator=args.separator, verbose=args.verbose,
                                                       no_nonce=args.no_nonce, option_strategy=args.option_strategy, num_options=args.num_options)

    datapath = pathlib.Path(args.datapath)
    output_dir = pathlib.Path(args.output_dir) if args.output_dir is not None else datapath.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    morph_data_path_stem = output_dir / f"{datapath.stem}{DATA_PROCESSOR_MAP[args.processor][1]}{args.suffix}"

    size_by_affix_len = {}
    size_by_prefix_len = {}
    size_by_suffix_len = {}

    for sample in morph_data:
        prefix_len = len(sample.get("prefixes", []))
        suffix_len = len(sample.get("suffixes", []))
        affix_len = prefix_len + suffix_len
        size_by_prefix_len[prefix_len] = size_by_prefix_len.get(prefix_len, 0) + 1
        size_by_suffix_len[suffix_len] = size_by_suffix_len.get(suffix_len, 0) + 1
        size_by_affix_len[affix_len] = size_by_affix_len.get(affix_len, 0) + 1
    
    morph_data = sorted(morph_data, key=lambda x: len(x.get("prefixes", [])) + len(x.get("suffixes", [])))

    output_data = {
        "metadata": {
            "source": args.datapath,
            "processor": args.processor,
            "language": input_data["metadata"]["language"],
            "size_by_affix_len": {i: size_by_affix_len.get(i, 0) for i in range(max(size_by_affix_len.keys()) + 1)},
            "size_by_prefix_len": {i: size_by_prefix_len.get(i, 0) for i in range(max(size_by_prefix_len.keys()) + 1)},
            "size_by_suffix_len": {i: size_by_suffix_len.get(i, 0) for i in range(max(size_by_suffix_len.keys()) + 1)}
        },
        "data": morph_data
    }

    write_json(output_data, morph_data_path_stem.with_suffix(".json"), ensure_ascii=False)

if __name__ == "__main__":
    main()