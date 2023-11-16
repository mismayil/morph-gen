import sys
import argparse
import pathlib
from tqdm import tqdm
import pandas as pd
import random

from utils import read_json, write_json

LANGUAGE_MAP = {
    "tr": "Turkish",
}

BLANK_FILLING_INSTRUCTION_TEMPLATE = "You are given a sentence in {language} with missing words and your task is to fill in the blanks with the words constructed from the given word roots and suffixes. You are allowed to use only the given words and suffixes. Output only the missing words inside square brackets separated by commas according to their order in the given sentence."

BLANK_FILLING_SHOT_TEMPLATE = """Example {index}:
Sentence: "{sentence}"
Words: {words}
Suffixes: {suffixes}
Missing words: {missing_words}
"""

INSTRUCTION_TEMPLATES = {
    "bfill": BLANK_FILLING_INSTRUCTION_TEMPLATE,
}

SHOT_TEMPLATES = {
    "bfill": BLANK_FILLING_SHOT_TEMPLATE,
}

SHOT_SAMPLES = [
    {
        "sentence": "Marilyn Monroe ___ hep güzel sarışın olarak kaldı",
        "words": ["akıl"],
        "suffixes": ["de", "lar", "da", "ler"],
        "missing_words": ["akıllarda"],
        "template": "bfill"
    },
    {
        "sentence": "Kitap, dizi kadar hatta belki diziden de ___",
        "words": ["sürükle"],
        "suffixes": ["dı", "ydi", "ydı", "di", "yici", "ici", "ıcı", "yıcı"],
        "missing_words": ["sürükleyiciydi"],
        "template": "bfill"
    },
    {
        "sentence": "Babacan diyorum çünkü çocukluğumuzda bizi hep kucaklardı, ___ ses çıkarmayan yaşlı bir dede edası ile kavuklarının arasında zıplayıp oyunlar uydurmamıza izin verirdi",
        "words": ["yaramaz"],
        "suffixes": ["ımız", "a", "lik", "imiz", "lar", "na", "ler", "ümüz", "lık", "e", "ne", "luk", "lük", "umuz"],
        "missing_words": ["yaramazlıklarımıza"],
        "template": "bfill"
    }
]

def prepare_sample_for_bfill(sample, shot_samples, template, language):
    shots = []

    for idx, shot_sample in enumerate(shot_samples):
        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            sentence=shot_sample["sentence"],
            words=str(shot_sample["words"]),
            suffixes=str(shot_sample["suffixes"]),
            missing_words=str(shot_sample["missing_words"]),
        )
        shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    eval_data = []

    final_shot = SHOT_TEMPLATES[template].format(
        index=len(shot_samples)+1,
        sentence=sample["sentence"],
        words=str(sample["words"]),
        suffixes=str(sample["suffixes"]),
        missing_words="",
    )
    
    prompt = f"{INSTRUCTION_TEMPLATES[template].format(language=LANGUAGE_MAP[language])}\n\n{shots_prompt}\n\n{final_shot}"
    
    eval_data.append({
        "id": sample["id"],
        "sentence": sample["sentence"],
        "words": sample["words"],
        "suffixes": sample["suffixes"],
        "prompt": prompt,
        "gold_answer": sample["missing_words"],
        "template": template
    })

    return eval_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("--template", type=str, default="bfill")
    parser.add_argument("--num-shots", type=int, default=3)
    parser.add_argument("--language", type=str, default="tr")
    parser.add_argument("--suffix", type=str, default="", help="Custom suffix for output file path.")

    args = parser.parse_args()
    results = read_json(args.datapath)

    eval_data = []

    shot_samples = [sample for sample in SHOT_SAMPLES if sample["template"] == args.template][:args.num_shots]

    if not shot_samples:
        shot_samples = results[:args.num_shots]

    for result in tqdm(results, desc="Preparing results for LLM evaluation"):
        if args.template == "bfill":
            eval_data.extend(prepare_sample_for_bfill(result, shot_samples, args.template, args.language))
        else:
            raise NotImplementedError(f"Template {args.template} is not implemented.")

    datapath = pathlib.Path(args.datapath)
    eval_data_path_stem = datapath.parent / f"{datapath.stem}_llm_{args.template}{args.suffix}"

    write_json(eval_data, eval_data_path_stem.with_suffix(".json"))
    pd.DataFrame(eval_data).to_csv(eval_data_path_stem.with_suffix(".csv"), index=False)

if __name__ == "__main__":
    main()