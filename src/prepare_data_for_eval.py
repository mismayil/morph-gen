import sys
import argparse
import pathlib
from tqdm import tqdm
import random

from utils import read_json, write_json
from prompts import MORPH_GEN_EN_INSTRUCTION_TEMPLATE, MORPH_GEN_EN_SHOT_TEMPLATE, MORPH_DISC_EN_INSTRUCTION_TEMPLATE, MORPH_DISC_EN_SHOT_TEMPLATE

LANGUAGE_MAP = {
    "tr": "Turkish",
    "en": "English",
}

INSTRUCTION_TEMPLATES = {
    "morph_gen_en": MORPH_GEN_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_en": MORPH_DISC_EN_INSTRUCTION_TEMPLATE,
}

SHOT_TEMPLATES = {
    "morph_gen_en": MORPH_GEN_EN_SHOT_TEMPLATE,
    "morph_disc_en": MORPH_DISC_EN_SHOT_TEMPLATE,
}

def prepare_sample_for_morph_gen(sample, shot_samples, template, language):
    shots = []

    for idx, shot_sample in enumerate(shot_samples):
        suffixes = random.sample(shot_sample["suffixes"], len(shot_sample["suffixes"]))
        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            root=shot_sample["root"],
            suffixes=",".join(suffixes),
            answer=shot_sample["derivation"],
            # pos=POS_MAP[shot_sample["pos"]],
        )
        shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    eval_data = []

    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    final_shot = SHOT_TEMPLATES[template].format(
        index=len(shot_samples)+1,
        root=sample["root"],
        suffixes=",".join(suffixes),
        # pos=POS_MAP[sample["pos"]],
        answer="",
    )
    
    prompt = f"{INSTRUCTION_TEMPLATES[template].format(language=LANGUAGE_MAP[language])}\n\n{shots_prompt}\n\n{final_shot}"
    
    eval_data.append({
        "root": sample["root"],
        "suffixes": sample["suffixes"],
        "prompt": prompt,
        "reference": sample["derivation"],
        "template": template,
        "original_root": sample["original_root"] if "original_root" in sample else None
    })

    return eval_data

def prepare_sample_for_morph_disc(sample, shot_samples, template, language):
    shots = []

    for idx, shot_sample in enumerate(shot_samples):
        options = random.sample(shot_sample["options"], len(shot_sample["options"]))
        suffixes = random.sample(shot_sample["suffixes"], len(shot_sample["suffixes"]))

        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            root=shot_sample["root"],
            suffixes=",".join(suffixes),
            # pos=POS_MAP[shot_sample["pos"]],
            options="\n".join([f"{o_index+1}. {option}" for o_index, option in enumerate(options)]),
            answer=options.index(shot_sample["derivation"])+1,
        )
        shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    eval_data = []

    options = random.sample(sample["options"], len(sample["options"]))

    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    final_shot = SHOT_TEMPLATES[template].format(
        index=len(shot_samples)+1,
        root=sample["root"],
        suffixes=",".join(suffixes),
        # pos=POS_MAP[sample["pos"]],
        options="\n".join([f"{o_index+1}. {option}" for o_index, option in enumerate(options)]),
        answer="",
    )
    
    prompt = f"{INSTRUCTION_TEMPLATES[template].format(language=LANGUAGE_MAP[language])}\n\n{shots_prompt}\n\n{final_shot}"
    
    eval_data.append({
        "root": sample["root"],
        "suffixes": sample["suffixes"],
        "prompt": prompt,
        "reference": options.index(sample["derivation"])+1,
        "template": template,
        "original_root": sample["original_root"] if "original_root" in sample else None
    })

    return eval_data

TEMPLATE_PROCESSOR_MAP = {
    "morph_gen_en": prepare_sample_for_morph_gen,
    "morph_disc_en": prepare_sample_for_morph_disc,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("-t", "--template", type=str, default="morph_gen_en", help="Template name")
    parser.add_argument("-n", "--num-shots", type=int, default=1)
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")

    args = parser.parse_args()
    input_data = read_json(args.datapath)

    eval_data = []

    shot_samples = input_data["data"][:args.num_shots]

    for sample in tqdm(input_data["data"], desc="Preparing input_data for evaluation"):
        eval_data.extend(TEMPLATE_PROCESSOR_MAP[args.template](sample, shot_samples, args.template, input_data["metadata"]["language"]))

    datapath = pathlib.Path(args.datapath)
    output_dir = pathlib.Path(args.output_dir) if args.output_dir is not None else datapath.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    eval_data_path_stem = output_dir / f"{datapath.stem}_eval_{args.template}_s{args.num_shots}{args.suffix}"

    output_data = {
        "metadata": {
            "source": args.datapath,
            "template": args.template,
            "language": input_data["metadata"]["language"],
            "num_shots": args.num_shots
        },
        "data": eval_data
    }
    write_json(output_data, eval_data_path_stem.with_suffix(".json"), ensure_ascii=False)

if __name__ == "__main__":
    main()