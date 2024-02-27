import sys
import argparse
import pathlib
from tqdm import tqdm
import random

from utils import read_json, write_json
from prompts import *

LANGUAGE_MAP = {
    "tr": {
        "en": "Turkish",
        "tr": "Türkçe"
    },
    "en": {
        "en": "English",
        "tr": "İngilizce"
    }
}

INSTRUCTION_TEMPLATES = {
    "morph_gen_en": MORPH_GEN_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_en": MORPH_DISC_EN_INSTRUCTION_TEMPLATE,
    "morph_gen_tr": MORPH_GEN_TR_INSTRUCTION_TEMPLATE,
    "morph_disc_tr": MORPH_DISC_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_en": MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_en": MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_tr": MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_tr": MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE,
    "morph_gen_order_en": MORPH_GEN_ORDER_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_order_en": MORPH_GEN_NONCE_ORDER_EN_INSTRUCTION_TEMPLATE
}

SHOT_TEMPLATES = {
    "morph_gen_en": MORPH_GEN_EN_SHOT_TEMPLATE,
    "morph_disc_en": MORPH_DISC_EN_SHOT_TEMPLATE,
    "morph_gen_tr": MORPH_GEN_TR_SHOT_TEMPLATE,
    "morph_disc_tr": MORPH_DISC_TR_SHOT_TEMPLATE,
    "nonce_morph_gen_en": MORPH_GEN_NONCE_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_en": MORPH_DISC_NONCE_EN_SHOT_TEMPLATE,
    "nonce_morph_gen_tr": MORPH_GEN_NONCE_TR_SHOT_TEMPLATE,
    "nonce_morph_disc_tr": MORPH_DISC_NONCE_TR_SHOT_TEMPLATE,
    "morph_gen_order_en": MORPH_GEN_EN_SHOT_TEMPLATE,
    "nonce_morph_gen_order_en": MORPH_GEN_NONCE_EN_SHOT_TEMPLATE
}

def _is_ood_sample(sample):
    return sample.get("original_root", None) is not None

def _get_sample_definition(sample, language, template_lang):
    if template_lang == "en":
        return f"'{sample['root']}' means '{sample['original_root']}' in {LANGUAGE_MAP[language][template_lang]}."
    elif template_lang == "tr":
        return f"'{sample['root']}' {LANGUAGE_MAP[language][template_lang]} '{sample['original_root']}' anlamına gelir."

def _get_template_lang(template):
    return template.split("_")[-1]

def prepare_shot_for_morph_gen(idx, sample, template, language, is_final=False):
    template_lang = _get_template_lang(template)
    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    suffixes_str = ", ".join([f"'{s}'" for s in suffixes])
    answer = sample["derivation"]

    if _is_ood_sample(sample):
        definition = _get_sample_definition(sample, language, template_lang)
        shot = SHOT_TEMPLATES[f"nonce_{template}"].format(
            index=idx+1,
            root=sample["root"],
            definition=definition,
            suffixes=suffixes_str,
            answer="" if is_final else answer,
        )
    else:
        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            root=sample["root"],
            suffixes=suffixes_str,
            answer="" if is_final else answer,
        )
    
    return shot, answer

def prepare_shot_for_morph_gen_order(idx, sample, template, language, is_final=False):
    template_lang = _get_template_lang(template)
    suffixes = random.sample([(i, s) for i, s in enumerate(sample["suffixes"])], len(sample["suffixes"]))
    suffixes_str = ", ".join([f"{i+1}. '{s[1]}'" for i, s in enumerate(suffixes)])
    answer = ",".join([str(idx[1]) for idx in sorted(zip([i_s[0] for i_s in suffixes], range(1, len(suffixes)+1)), key=lambda x: x[0])])

    if _is_ood_sample(sample):
        definition = _get_sample_definition(sample, language, template_lang)
        shot = SHOT_TEMPLATES[f"nonce_{template}"].format(
            index=idx+1,
            root=sample["root"],
            definition=definition,
            suffixes=suffixes_str,
            answer="" if is_final else answer,
        )
    else:
        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            root=sample["root"],
            suffixes=suffixes_str,
            answer="" if is_final else answer,
        )
    
    return shot, answer

def prepare_instruction_for_morph_gen_disc(sample, template, language):
    instruction_template = INSTRUCTION_TEMPLATES[template]
    template_lang = _get_template_lang(template)

    if _is_ood_sample(sample):
        instruction_template = INSTRUCTION_TEMPLATES[f"nonce_{template}"]

    return instruction_template.format(language=LANGUAGE_MAP[language][template_lang])

def prepare_shot_for_morph_disc(idx, sample, template, language, is_final=False):
    options = random.sample(sample["options"], len(sample["options"]))
    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    template_lang = _get_template_lang(template)
    suffixes_str = ",".join([f"'{s}'" for s in suffixes])
    options_str = "\n".join([f"{o_index+1}. {option}" for o_index, option in enumerate(options)])
    answer = options.index(sample["derivation"])+1

    if _is_ood_sample(sample):
        definition = _get_sample_definition(sample, language, template_lang)
        shot = SHOT_TEMPLATES[f"nonce_{template}"].format(
            index=idx+1,
            root=sample["root"],
            definition=definition,
            suffixes=suffixes_str,
            options=options_str,
            answer="" if is_final else answer,
        )
    else:
        shot = SHOT_TEMPLATES[template].format(
            index=idx+1,
            root=sample["root"],
            suffixes=suffixes_str,
            options=options_str,
            answer="" if is_final else answer,
        )
    
    return shot, answer

INSTRUCTION_PROCESSORS = {
    "morph_gen_en": prepare_instruction_for_morph_gen_disc,
    "morph_disc_en": prepare_instruction_for_morph_gen_disc,
    "morph_gen_tr": prepare_instruction_for_morph_gen_disc,
    "morph_disc_tr": prepare_instruction_for_morph_gen_disc,
    "morph_gen_order_en": prepare_instruction_for_morph_gen_disc,
}

SHOT_PROCESSORS = {
    "morph_gen_en": prepare_shot_for_morph_gen,
    "morph_disc_en": prepare_shot_for_morph_disc,
    "morph_gen_tr": prepare_shot_for_morph_gen,
    "morph_disc_tr": prepare_shot_for_morph_disc,
    "morph_gen_order_en": prepare_shot_for_morph_gen_order,
}

def prepare_sample_for_eval(sample, shot_samples, template, language):
    shot_processor = SHOT_PROCESSORS[template]
    instruction_processor = INSTRUCTION_PROCESSORS[template]

    shots = []
    for idx, shot_sample in enumerate(shot_samples):
        shot, _ = shot_processor(idx, shot_sample, template, language)
        shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    final_shot, final_answer = shot_processor(len(shot_samples), sample, template, language, is_final=True)
    
    instruction = instruction_processor(sample, template, language)

    prompt = f"{instruction}\n\n{shots_prompt}\n\n{final_shot}"
    
    eval_data = []
    eval_data.append({
        "id": sample["id"],
        "root": sample["root"],
        "suffixes": sample["suffixes"],
        "prompt": prompt,
        "reference": final_answer,
        "template": template,
        "original_root": sample["original_root"] if "original_root" in sample else None
    })

    return eval_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("-t", "--template", type=str, default="morph_gen_en", help="Template name")
    parser.add_argument("-n", "--num-shots", type=int, default=1)
    parser.add_argument("-s", "--suffix", type=str, default="", help="Custom suffix for output file path.")
    parser.add_argument("-o", "--output-dir", type=str, default=None, help="Output directory path. Defaults to input directory path.")
    parser.add_argument("-m", "--match-len", action="store_true", help="Match length of suffixes in shots and prompts.")

    args = parser.parse_args()
    input_data = read_json(args.datapath)

    eval_data = []

    shot_samples = input_data["data"][:args.num_shots]

    for sample in tqdm(input_data["data"], desc="Preparing input_data for evaluation"):
        if args.match_len:
            shot_samples = [shot for shot in input_data["data"] if len(shot["suffixes"]) == len(sample["suffixes"]) and shot["id"] != sample["id"]][:args.num_shots]
        
        if sample.get("similar"):
            shot_samples = sample["similar"]

        if shot_samples:
            eval_data.extend(prepare_sample_for_eval(sample, shot_samples, args.template, input_data["metadata"]["language"]))

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