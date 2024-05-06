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
    "nonce_morph_gen_order_en": MORPH_GEN_NONCE_ORDER_EN_INSTRUCTION_TEMPLATE,
    "morph_gen_sent_en": MORPH_GEN_SENT_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_sent_en": MORPH_DISC_SENT_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_sent_en": MORPH_GEN_NONCE_SENT_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_sent_en": MORPH_DISC_NONCE_SENT_EN_INSTRUCTION_TEMPLATE,
    "morph_gen_sent_tr": MORPH_GEN_SENT_TR_INSTRUCTION_TEMPLATE,
    "morph_disc_sent_tr": MORPH_DISC_SENT_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_sent_tr": MORPH_GEN_NONCE_SENT_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_sent_tr": MORPH_DISC_NONCE_SENT_TR_INSTRUCTION_TEMPLATE,
    "morph_gen_sense_en": MORPH_GEN_SENSE_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_sense_en": MORPH_DISC_SENSE_EN_INSTRUCTION_TEMPLATE,
    "morph_gen_sense_tr": MORPH_GEN_SENSE_TR_INSTRUCTION_TEMPLATE,
    "morph_disc_sense_tr": MORPH_DISC_SENSE_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_sense_en": MORPH_GEN_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_sense_en": MORPH_DISC_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_sense_tr": MORPH_GEN_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_sense_tr": MORPH_DISC_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE,
    "morph_disc_mcq_en": MORPH_DISC_MCQ_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_mcq_tr": MORPH_DISC_MCQ_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_mcq_en": MORPH_DISC_MCQ_NONCE_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_mcq_tr": MORPH_DISC_MCQ_NONCE_TR_INSTRUCTION_TEMPLATE,
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
    "nonce_morph_gen_order_en": MORPH_GEN_NONCE_EN_SHOT_TEMPLATE,
    "morph_gen_sent_en": MORPH_GEN_SENT_EN_SHOT_TEMPLATE,
    "morph_disc_sent_en": MORPH_DISC_SENT_EN_SHOT_TEMPLATE,
    "nonce_morph_gen_sent_en": MORPH_GEN_NONCE_SENT_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_sent_en": MORPH_DISC_NONCE_SENT_EN_SHOT_TEMPLATE,
    "morph_gen_sent_tr": MORPH_GEN_SENT_TR_SHOT_TEMPLATE,
    "morph_disc_sent_tr": MORPH_DISC_SENT_TR_SHOT_TEMPLATE,
    "nonce_morph_gen_sent_tr": MORPH_GEN_NONCE_SENT_TR_SHOT_TEMPLATE,
    "nonce_morph_disc_sent_tr": MORPH_DISC_NONCE_SENT_TR_SHOT_TEMPLATE,
    "morph_gen_sense_en": MORPH_GEN_SENSE_EN_SHOT_TEMPLATE,
    "morph_disc_sense_en": MORPH_DISC_SENSE_EN_SHOT_TEMPLATE,
    "morph_gen_sense_tr": MORPH_GEN_SENSE_TR_SHOT_TEMPLATE,
    "morph_disc_sense_tr": MORPH_DISC_SENSE_TR_SHOT_TEMPLATE,
    "nonce_morph_gen_sense_en": MORPH_GEN_NONCE_SENSE_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_sense_en": MORPH_DISC_NONCE_SENSE_EN_SHOT_TEMPLATE,
    "nonce_morph_gen_sense_tr": MORPH_GEN_NONCE_SENSE_TR_SHOT_TEMPLATE,
    "nonce_morph_disc_sense_tr": MORPH_DISC_NONCE_SENSE_TR_SHOT_TEMPLATE,
    "morph_disc_mcq_en": MORPH_DISC_MCQ_EN_SHOT_TEMPLATE,
    "morph_disc_mcq_tr": MORPH_DISC_MCQ_TR_SHOT_TEMPLATE,
    "nonce_morph_disc_mcq_en": MORPH_DISC_MCQ_NONCE_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_mcq_tr": MORPH_DISC_MCQ_NONCE_TR_SHOT_TEMPLATE,
}

def _is_ood_sample(sample):
    return sample.get("original_root", None) is not None

def _is_sense_task(template):
    return "sense" in template

def _is_sent_task(template):
    return "sent" in template

def _get_root_definition(sample, language, template, template_lang):
    if template_lang == "en":
        return f"{sample['root']} means {sample['original_root']} in {LANGUAGE_MAP[language][template_lang]}."
    elif template_lang == "tr":
        return f"{sample['root']} {LANGUAGE_MAP[language][template_lang]} {sample['original_root']} anlamına gelir."

def _get_target_definition(sample, language, template, template_lang):
    return sample.get("meaning", None)

def _get_template_lang(template):
    return template.split("_")[-1]

def _get_answer(option, reference, template_lang):
    correct = option == reference
    if template_lang == "en":
        return "Yes" if correct else "No"
    elif template_lang == "tr":
        return "Evet" if correct else "Hayır"

def prepare_shot_for_morph_gen(idx, sample, template, language, is_final=False):
    template_lang = _get_template_lang(template)
    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    suffixes_str = ", ".join([f"{s}" for s in suffixes])
    answer = sample["derivation"]

    format_args = {
        "index": idx+1,
        "root": sample["root"],
        "suffixes": suffixes_str,
        "answer": "" if is_final else answer
    }
    shot_template = SHOT_TEMPLATES[template]
    
    if _is_ood_sample(sample):
        definition = _get_root_definition(sample, language, template, template_lang)
        format_args["root_definition"] = definition
        shot_template = SHOT_TEMPLATES[f"nonce_{template}"]

    if _is_sent_task(template):
        format_args["sentence"] = sample["sentence"]

    if _is_sense_task(template):
        definition = _get_target_definition(sample, language, template, template_lang)
        format_args["target_definition"] = definition

    shot = shot_template.format(**format_args)
    
    return shot, answer

def prepare_shot_for_morph_gen_order(idx, sample, template, language, is_final=False):
    template_lang = _get_template_lang(template)
    suffixes = random.sample([(i, s) for i, s in enumerate(sample["suffixes"])], len(sample["suffixes"]))
    suffixes_str = ", ".join([f"{i+1}. {s[1]}" for i, s in enumerate(suffixes)])
    answer = ",".join([str(idx[1]) for idx in sorted(zip([i_s[0] for i_s in suffixes], range(1, len(suffixes)+1)), key=lambda x: x[0])])

    format_args = {
        "index": idx+1,
        "root": sample["root"],
        "suffixes": suffixes_str,
        "answer": "" if is_final else answer
    }
    shot_template = SHOT_TEMPLATES[template]

    if _is_ood_sample(sample):
        definition = _get_root_definition(sample, language, template, template_lang)
        format_args["root_definition"] = definition
        shot_template = SHOT_TEMPLATES[f"nonce_{template}"]

    if _is_sent_task(template):
        format_args["sentence"] = sample["sentence"]

    if _is_sense_task(template):
        definition = _get_target_definition(sample, language, template, template_lang)
        format_args["target_definition"] = definition

    shot = shot_template.format(**format_args)
    
    return shot, answer

def prepare_instruction_for_morph_gen_disc(sample, template, language):
    instruction_template = INSTRUCTION_TEMPLATES[template]
    template_lang = _get_template_lang(template)

    if _is_ood_sample(sample):
        instruction_template = INSTRUCTION_TEMPLATES[f"nonce_{template}"]

    return instruction_template.format(language=LANGUAGE_MAP[language][template_lang])

def prepare_shot_for_morph_disc_mcq(idx, sample, template, language, is_final=False):
    options = random.sample(sample["options"], len(sample["options"]))
    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    template_lang = _get_template_lang(template)
    suffixes_str = ",".join([f"{s}" for s in suffixes])
    options_str = "\n".join([f"{o_index+1}. {option}" for o_index, option in enumerate(options)])
    answer = options.index(sample["derivation"])+1

    format_args = {
        "index": idx+1,
        "root": sample["root"],
        "suffixes": suffixes_str,
        "options": options_str,
        "answer": "" if is_final else answer
    }
    shot_template = SHOT_TEMPLATES[template]

    if _is_ood_sample(sample):
        definition = _get_root_definition(sample, language, template, template_lang)
        format_args["root_definition"] = definition
        shot_template = SHOT_TEMPLATES[f"nonce_{template}"]

    if _is_sent_task(template):
        format_args["sentence"] = sample["sentence"]

    if _is_sense_task(template):
        definition = _get_target_definition(sample, language, template, template_lang)
        format_args["target_definition"] = definition

    shot = shot_template.format(**format_args)
    
    return shot, answer

def prepare_shots_for_morph_disc(idx, sample, template, language, is_final=False):
    options = random.sample(sample["options"], len(sample["options"]))
    suffixes = random.sample(sample["suffixes"], len(sample["suffixes"]))
    template_lang = _get_template_lang(template)
    suffixes_str = ",".join([f"{s}" for s in suffixes])

    shots = []
    answers = []

    for option in options:
        answer = _get_answer(option, sample["derivation"], template_lang)
        format_args = {
            "index": idx+1,
            "root": sample["root"],
            "suffixes": suffixes_str,
            "derived_word": option,
            "answer": "" if is_final else answer
        }
        shot_template = SHOT_TEMPLATES[template]

        if _is_ood_sample(sample):
            definition = _get_root_definition(sample, language, template, template_lang)
            format_args["root_definition"] = definition
            shot_template = SHOT_TEMPLATES[f"nonce_{template}"]

        if _is_sent_task(template):
            format_args["sentence"] = sample["sentence"]

        if _is_sense_task(template):
            definition = _get_target_definition(sample, language, template, template_lang)
            format_args["target_definition"] = definition

        shot = shot_template.format(**format_args)
        
        shots.append(shot)
        answers.append(answer)
    
    return shots, answers

INSTRUCTION_PROCESSORS = {
    "default": prepare_instruction_for_morph_gen_disc
}

SHOT_PROCESSORS = {
    "default_gen": prepare_shot_for_morph_gen,
    "default_disc": prepare_shots_for_morph_disc,
    "morph_gen_order_en": prepare_shot_for_morph_gen_order,
    "morph_disc_mcq_en": prepare_shot_for_morph_disc_mcq,
    "morph_disc_mcq_tr": prepare_shot_for_morph_disc_mcq
}

def _choose_answer_based_on_template(template_lang, idx):
    if template_lang == "en":
        return ["Yes", "No"][idx%2]
    elif template_lang == "tr":
        return ["Evet", "Hayır"][idx%2]

def _choose_shot_based_on_answer(shots, answers, chosen_answer):
    for shot, answer in zip(shots, answers):
        if answer == chosen_answer:
            return shot, answer
    return shots[0], answers[0]
 
def prepare_sample_for_eval(sample, shot_samples, template, language):
    shot_processor = SHOT_PROCESSORS.get(template, SHOT_PROCESSORS["default_gen"] if template.startswith("morph_gen") else SHOT_PROCESSORS["default_disc"])
    instruction_processor = INSTRUCTION_PROCESSORS.get(template, INSTRUCTION_PROCESSORS["default"])

    shots = []
    for idx, shot_sample in enumerate(shot_samples):
        shot, answer = shot_processor(idx, shot_sample, template, language)
        if isinstance(shot, list):
            chosen_answer = _choose_answer_based_on_template(_get_template_lang(template), idx)
            chosen_shot, _ = _choose_shot_based_on_answer(shot, answer, chosen_answer)
            shots.append(chosen_shot)
        else:
            shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    final_shot, final_answer = shot_processor(len(shot_samples), sample, template, language, is_final=True)
    
    if not isinstance(final_shot, list):
        final_shot = [final_shot]
    
    if not isinstance(final_answer, list):
        final_answer = [final_answer]
    
    eval_data = []
        
    for final_sh, final_ans in zip(final_shot, final_answer):
        instruction = instruction_processor(sample, template, language)

        prompt = f"{instruction}\n\n{shots_prompt}\n\n{final_sh}"

        eval_data.append({
            "id": sample["id"],
            "root": sample["root"],
            "suffixes": sample["suffixes"],
            "prompt": prompt,
            "reference": final_ans,
            "template": template,
            "original_root": sample["original_root"] if "original_root" in sample else None,
            "original_derivation": sample["original_derivation"] if "original_derivation" in sample else None,
            "meta_suffixes": sample.get("meta_suffixes", None),
            "sentence": sample.get("sentence", None),
            "meaning": sample.get("meaning", None),
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