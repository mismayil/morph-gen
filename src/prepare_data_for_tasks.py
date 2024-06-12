import argparse
import json
import pathlib
import random
import sys
from itertools import permutations

from tqdm import tqdm

from morphology import (
    generate_nonce_word_en,
    generate_nonce_word_tr,
    read_en_dictionary,
    segment_by_tokenizer,
)
from utils import levenshtein_distance, read_json, write_json

NONCE_GENERATOR = {"tr": generate_nonce_word_tr, "en": generate_nonce_word_en}


def prepare_sample_for_tasks(
    sample, separator="", language="tr", verbose=False, no_nonce=False
):
    dictionary = read_en_dictionary()
    suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
    ref_derivation = sample["root"] + separator + separator.join(suffixes)

    if len(suffixes) > 0:
        suffix_perms = list(permutations(suffixes))
        options = set()

        for suffix_perm in suffix_perms:
            derivation = sample["root"] + separator + separator.join(suffix_perm)

            if derivation != ref_derivation:
                options.add(derivation)

        # options = random.sample(list(options), min(len(options), 5))
        options = sorted(
            list(options), key=lambda x: levenshtein_distance(x, ref_derivation)
        )[:5]
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
            "pos": sample["pos"],
            "suffixes": suffixes,
            "derivation": ref_derivation,
            "positive_options": [ref_derivation],
            "negative_options": list(options),
            "answer": 0,
            "meta_suffixes": sample.get("meta_morphemes"),
            "sentence": (
                sentence.lower().replace(ref_derivation, "___") if sentence else None
            ),
            "meaning": sample.get("meaning"),
        }

    return None


def prepare_data_for_tasks(
    input_data,
    num_samples=None,
    separator="",
    verbose=False,
    no_nonce=False,
    *args,
    **kwargs,
):
    data = input_data["data"]
    language = input_data["metadata"]["language"]

    morph_data = []

    for i, sample in tqdm(
        enumerate(data), total=len(data), desc="Preparing data TR for Morph tasks"
    ):
        morph_sample = prepare_sample_for_tasks(
            sample, separator, language=language, verbose=verbose, no_nonce=no_nonce
        )

        if morph_sample is not None:
            morph_data.append(morph_sample)

    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data


def prepare_nonce_data_for_tasks(input_data, num_samples=None, *args, **kwargs):
    data = input_data["data"]
    nonce_data = []

    for i, sample in tqdm(
        enumerate(data), total=len(data), desc="Preparing TR nonce data for Morph tasks"
    ):
        id_root = sample["id_root"]
        pos = sample["pos"]
        suffixes = sample["morphemes"] if "morphemes" in sample else sample["suffixes"]
        derivation = sample["derivation"]
        positive_options = sample["positive_options"]
        negative_options = sample["negative_options"]
        ood_root = sample["ood_root"]

        nonce_derivation = derivation.replace(id_root, ood_root, 1)

        nonce_data.append(
            {
                "id": f"{sample['id']}-ood",
                "id_root": sample["id_root"],
                "id_derivation": derivation,
                "ood_root": ood_root,
                "root": ood_root,
                "pos": pos,
                "suffixes": suffixes,
                "derivation": nonce_derivation,
                "positive_options": [
                    option.replace(id_root, ood_root, 1) for option in positive_options
                ],
                "negative_options": [
                    option.replace(id_root, ood_root, 1) for option in negative_options
                ],
                "answer": 0,
                "similar": sample.get("similar"),
                "meta_suffixes": (
                    sample.get("meta_morphemes")
                    if "meta_morphemes" in sample
                    else sample.get("meta_suffixes")
                ),
                "sentence": sample.get("sentence"),
                "meaning": sample.get("meaning"),
                "negative_suffixes": sample.get("negative_suffixes"),
                "negative_meta_suffixes": sample.get("negative_meta_suffixes"),
            }
        )

    if num_samples is not None:
        nonce_data = random.sample(nonce_data, num_samples)

    return nonce_data


def prepare_tr_comp_data_for_tasks(
    input_data, num_samples=None, separator="", *args, **kwargs
):
    data = input_data["data"]

    morph_data = []

    for i, samples in tqdm(
        enumerate(data), desc="Preparing comp data TR for Morph tasks"
    ):
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
                morph_data.append(
                    {
                        "id": f"tr-comp-{i}",
                        **prepare_sample_for_tasks(ref_sample, separator),
                        "similar": similar_samples,
                    }
                )

    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data


def prepare_tok_aligned_data_for_tasks(
    input_data, num_samples=None, separator="", model="gpt-4", *args, **kwargs
):
    data = input_data["data"]
    tok_aligned_data = []

    for i, sample in tqdm(
        enumerate(data),
        total=len(data),
        desc="Preparing tokenization aligned data for tasks",
    ):
        ref_derivation = sample["derivation"]
        tokens = segment_by_tokenizer(ref_derivation, model, sample["root"])
        root_token = tokens[0]
        token_perms = permutations(tokens[1:])
        options = set()

        for token_perm in token_perms:
            derivation = root_token + separator + separator.join(token_perm)

            if derivation != ref_derivation:
                options.add(derivation)

        options = sorted(
            list(options), key=lambda x: levenshtein_distance(x, ref_derivation)
        )[:5]
        tok_aligned_data.append(
            {
                **sample,
                "ref_root": sample["root"],
                "ref_suffixes": (
                    sample["suffixes"]
                    if "suffixes" in sample
                    else sample.get("morphemes")
                ),
                "root": root_token,
                "suffixes": tokens[1:],
                "negative_options": list(options),
            }
        )

    if num_samples is not None:
        tok_aligned_data = random.sample(tok_aligned_data, num_samples)

    return tok_aligned_data


def prepare_tr_sense_data_for_tasks(
    input_data, num_samples=None, separator="", *args, **kwargs
):
    data = input_data["data"]

    morph_data = []

    for i, sample in tqdm(
        enumerate(data), total=len(data), desc="Preparing data TR for Morph tasks"
    ):
        morph_sample = prepare_sample_for_tasks(sample, separator)

        if morph_sample is not None:
            meanings = [m for m in sample["meanings"] if len(m.split()) > 1]

            if meanings:
                morph_data.append(
                    {
                        "id": sample.get("id", f"tr-sense-{i}"),
                        **morph_sample,
                        "meaning": sample["meanings"][0],
                    }
                )

    if num_samples is not None:
        morph_data = random.sample(morph_data, num_samples)

    return morph_data


DATA_PROCESSOR_MAP = {
    "morph": (prepare_data_for_tasks, "_morph"),
    "morph_nonce": (prepare_nonce_data_for_tasks, "_nonce"),
    "tr_comp_morph": (prepare_tr_comp_data_for_tasks, "_morph"),
    "tok_aligned": (prepare_tok_aligned_data_for_tasks, "_tok_aligned"),
    "tr_sense": (prepare_tr_sense_data_for_tasks, "_sense"),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--datapath", type=str, help="Path to data", required=True
    )
    parser.add_argument(
        "-p", "--processor", type=str, default="pilot_morph", help="Data processor name"
    )
    parser.add_argument(
        "-n",
        "--num-samples",
        type=int,
        default=None,
        help="Number of samples to process",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        type=str,
        default="",
        help="Custom suffix for output file path.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default=None,
        help="Output directory path. Defaults to input directory path.",
    )
    parser.add_argument(
        "-t",
        "--separator",
        type=str,
        default="",
        help="Separator to use between morphemes. Defaults to empty string.",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument(
        "-nn", "--no-nonce", action="store_true", help="Do not generate nonce words"
    )

    args = parser.parse_args()
    input_data = read_json(args.datapath)
    morph_data = DATA_PROCESSOR_MAP[args.processor][0](
        input_data,
        args.num_samples,
        separator=args.separator,
        verbose=args.verbose,
        no_nonce=args.no_nonce,
    )

    datapath = pathlib.Path(args.datapath)
    output_dir = (
        pathlib.Path(args.output_dir)
        if args.output_dir is not None
        else datapath.parent
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    morph_data_path_stem = (
        output_dir
        / f"{datapath.stem}{DATA_PROCESSOR_MAP[args.processor][1]}{args.suffix}"
    )

    output_data = {
        "metadata": {
            "source": args.datapath,
            "processor": args.processor,
            "language": input_data["metadata"]["language"],
        },
        "data": morph_data,
    }

    write_json(
        output_data, morph_data_path_stem.with_suffix(".json"), ensure_ascii=False
    )


if __name__ == "__main__":
    main()
