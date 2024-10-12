import sys
import argparse
import pathlib
from tqdm import tqdm
import random

from utils import read_json, write_json
from prompts import *

LANGUAGE_MAP = {
    "tr": {"en": "Turkish", "tr": "Türkçe", "fi": "turkki"},
    "en": {"en": "English", "tr": "İngilizce", "fi": "englanti"},
    "fi": {"en": "Finnish", "tr": "Fince", "fi": "suomi"},
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
    "morph_disc_pp_en": MORPH_DISC_PP_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_cot_en": MORPH_DISC_COT_EN_INSTRUCTION_TEMPLATE,
    "morph_gen_cot_en": MORPH_GEN_COT_EN_INSTRUCTION_TEMPLATE,
    "morph_disc_cot_tr": MORPH_DISC_COT_TR_INSTRUCTION_TEMPLATE,
    "morph_gen_cot_tr": MORPH_GEN_COT_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_cot_en": MORPH_DISC_NONCE_COT_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_cot_en": MORPH_GEN_NONCE_COT_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_cot_tr": MORPH_DISC_NONCE_COT_TR_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_cot_tr": MORPH_GEN_NONCE_COT_TR_INSTRUCTION_TEMPLATE,
    "morph_gen_fi": MORPH_GEN_FI_INSTRUCTION_TEMPLATE,
    "morph_disc_fi": MORPH_DISC_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_fi": MORPH_GEN_NONCE_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_fi": MORPH_DISC_NONCE_FI_INSTRUCTION_TEMPLATE,
    "morph_gen_sent_fi": MORPH_GEN_SENT_FI_INSTRUCTION_TEMPLATE,
    "morph_disc_sent_fi": MORPH_DISC_SENT_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_sent_fi": MORPH_GEN_NONCE_SENT_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_sent_fi": MORPH_DISC_NONCE_SENT_FI_INSTRUCTION_TEMPLATE,
    "morph_gen_cot_fi": MORPH_GEN_COT_FI_INSTRUCTION_TEMPLATE,
    "morph_disc_cot_fi": MORPH_DISC_COT_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_gen_cot_fi": MORPH_GEN_NONCE_COT_FI_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_cot_fi": MORPH_DISC_NONCE_COT_FI_INSTRUCTION_TEMPLATE,
    "morph_disc_no_affix_en": MORPH_DISC_NO_AFFIX_EN_INSTRUCTION_TEMPLATE,
    "nonce_morph_disc_no_affix_en": MORPH_DISC_NONCE_NO_AFFIX_EN_INSTRUCTION_TEMPLATE
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
    "morph_disc_pp_en": MORPH_DISC_PP_EN_SHOT_TEMPLATE,
    "morph_disc_cot_en": MORPH_DISC_COT_EN_SHOT_TEMPLATE,
    "morph_gen_cot_en": MORPH_GEN_COT_EN_SHOT_TEMPLATE,
    "morph_disc_cot_tr": MORPH_DISC_COT_TR_SHOT_TEMPLATE,
    "morph_gen_cot_tr": MORPH_GEN_COT_TR_SHOT_TEMPLATE,
    "nonce_morph_disc_cot_en": MORPH_DISC_NONCE_COT_EN_SHOT_TEMPLATE,
    "nonce_morph_gen_cot_en": MORPH_GEN_NONCE_COT_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_cot_tr": MORPH_DISC_NONCE_COT_TR_SHOT_TEMPLATE,
    "nonce_morph_gen_cot_tr": MORPH_GEN_NONCE_COT_TR_SHOT_TEMPLATE,
    "morph_gen_fi": MORPH_GEN_FI_SHOT_TEMPLATE,
    "morph_disc_fi": MORPH_DISC_FI_SHOT_TEMPLATE,
    "nonce_morph_disc_fi": MORPH_DISC_NONCE_FI_SHOT_TEMPLATE,
    "nonce_morph_gen_fi": MORPH_GEN_NONCE_FI_SHOT_TEMPLATE,
    "morph_gen_sent_fi": MORPH_GEN_SENT_FI_SHOT_TEMPLATE,
    "morph_disc_sent_fi": MORPH_DISC_SENT_FI_SHOT_TEMPLATE,
    "nonce_morph_gen_sent_fi": MORPH_GEN_NONCE_SENT_FI_SHOT_TEMPLATE,
    "nonce_morph_disc_sent_fi": MORPH_DISC_NONCE_SENT_FI_SHOT_TEMPLATE,
    "morph_gen_cot_fi": MORPH_GEN_COT_FI_SHOT_TEMPLATE,
    "morph_disc_cot_fi": MORPH_DISC_COT_FI_SHOT_TEMPLATE,
    "nonce_morph_gen_cot_fi": MORPH_GEN_NONCE_COT_FI_SHOT_TEMPLATE,
    "nonce_morph_disc_cot_fi": MORPH_DISC_NONCE_COT_FI_SHOT_TEMPLATE,
    "morph_disc_no_affix_en": MORPH_DISC_NO_AFFIX_EN_SHOT_TEMPLATE,
    "nonce_morph_disc_no_affix_en": MORPH_DISC_NONCE_NO_AFFIX_EN_SHOT_TEMPLATE
}

def _is_ood_sample(sample):
    return sample["root"] == sample["ood_root"]

def _is_sense_task(template):
    return "sense" in template

def _is_sent_task(template):
    return "sent" in template

def _is_cot_task(template):
    return "cot" in template

def _get_root_definition(sample, language, template, template_lang):
    if template_lang == "en":
        return f"{sample['root']} means {sample['id_root']} in {LANGUAGE_MAP[language][template_lang]}."
    elif template_lang == "tr":
        return f"{sample['root']} {LANGUAGE_MAP[language][template_lang]} {sample['id_root']} anlamına gelir."
    elif template_lang == "fi":
        return f"{sample['root']} tarkoittaa {sample['id_root']} kielellä {LANGUAGE_MAP[language][template_lang]}."
    else:
        raise ValueError(f"Unknown language or template: {language}, {template_lang}")

def _get_target_definition(sample, language, template, template_lang):
    return sample.get("meaning", None)

def _get_template_lang(template):
    return template.split("_")[-1]

def _get_answer(option, reference, template_lang):
    correct = option in reference
    if template_lang == "en":
        return "Yes" if correct else "No"
    elif template_lang == "tr":
        return "Evet" if correct else "Hayır"
    elif template_lang == "fi":
        return "Kyllä" if correct else "Ei"
    else:
        raise ValueError(f"Unknown template language: {template_lang}")

def _get_affixes(sample):
    return sample.get("prefixes", []) + sample.get("suffixes", [])

def prepare_shot_for_morph_gen(
    idx,
    sample,
    template,
    language,
    is_final=False,
    shuffle_affixes=True,
    fixed_shots=False,
):
    template_lang = _get_template_lang(template)
    prefixes = sample.get("prefixes", [])
    suffixes = sample.get("suffixes", [])
    affixes = prefixes + suffixes

    if shuffle_affixes:
        if is_final or not fixed_shots:
            affixes = random.sample(affixes, len(affixes))

    affixes_str = ", ".join([f"{s}" for s in affixes])
    answer = sample["derivation"] if "positive_options" not in sample or _is_sent_task(template) or len(sample["positive_options"]) == 1 else sample["positive_options"]

    if _is_cot_task(template) and "cot_answer" in sample:
        answer = sample["cot_answer"]

    format_args = {
        "index": idx+1,
        "root": sample["root"],
        "affixes": affixes_str,
        "answer": "" if is_final else answer,
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


def prepare_shot_for_morph_disc_mcq(
    idx, sample, template, language, is_final=False, shuffle_affixes=True
):
    options = random.sample(sample["options"], len(sample["options"]))
    prefixes = sample.get("prefixes", [])
    suffixes = sample.get("suffixes", [])
    affixes = prefixes + suffixes

    if shuffle_affixes:
        affixes = random.sample(affixes, len(affixes))

    template_lang = _get_template_lang(template)
    affixes_str = ",".join([f"{s}" for s in affixes])
    options_str = "\n".join(
        [f"{o_index+1}. {option}" for o_index, option in enumerate(options)]
    )
    answer = options.index(sample["derivation"]) + 1

    format_args = {
        "index": idx+1,
        "root": sample["root"],
        "affixes": affixes_str,
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


def prepare_shots_for_morph_disc(
    idx,
    sample,
    template,
    language,
    is_final=False,
    shuffle_affixes=True,
    fixed_shots=False,
):
    template_lang = _get_template_lang(template)
    prefixes = sample.get("prefixes", []) or []
    suffixes = sample.get("suffixes", []) or []
    affixes = prefixes + suffixes
    negative_prefixes = sample.get("negative_prefixes", []) or []
    negative_suffixes = sample.get("negative_suffixes", []) or []
    negative_affixes = negative_prefixes + negative_suffixes
    reference = [sample["derivation"]]
    options = [sample["derivation"]]

    if shuffle_affixes:
        if is_final or not fixed_shots:
            affixes = random.sample(affixes, len(affixes))

            if negative_affixes:
                negative_affixes = random.sample(
                    negative_affixes, len(negative_affixes)
                )

    if "positive_options" in sample and "negative_options" in sample:
        if _is_sent_task(template):
            reference = [sample["positive_options"][0]]
            options = [sample["positive_options"][0]] + sample["negative_options"][:4]
        else:
            reference = sample["positive_options"]
            options = sample["positive_options"] + sample["negative_options"][:4]

    affixes_str = ", ".join([f"{s}" for s in affixes])
    negative_affixes_str = (
        ", ".join([f"{s}" for s in negative_affixes]) if negative_affixes else ""
    )

    shots = []
    answers = []

    for option in options:
        answer = (
            sample["cot_answer"]
            if _is_cot_task(template) and "cot_answer" in sample
            else _get_answer(option, reference, template_lang)
        )

        if template.startswith("morph_disc_pp"):
            format_args = {
                "text": option
            }
        else:
            format_args = {
                "index": idx+1,
                "root": sample["root"],
                "affixes": (
                    affixes_str
                    if not "positive_options" in sample or option in sample["positive_options"] or not negative_affixes_str
                    else negative_affixes_str
                ),
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
    "morph_disc_mcq_en": prepare_shot_for_morph_disc_mcq,
    "morph_disc_mcq_tr": prepare_shot_for_morph_disc_mcq
}

def _choose_answer_based_on_template(template_lang, idx):
    if template_lang == "en":
        return ["Yes", "No"][idx%2]
    elif template_lang == "tr":
        return ["Evet", "Hayır"][idx%2]
    elif template_lang == "fi":
        return ["Kyllä", "Ei"][idx%2]
    else:
        raise ValueError(f"Unknown template language: {template_lang}")

def _choose_shot_based_on_answer(shots, answers, chosen_answer):
    for shot, answer in zip(shots, answers):
        if answer == chosen_answer:
            return shot, answer
    return shots[0], answers[0]


def prepare_sample_for_eval(
    sample, shot_samples, template, language, shuffle_affixes=True, fixed_shots=False
):
    shot_processor = SHOT_PROCESSORS.get(
        template,
        (
            SHOT_PROCESSORS["default_gen"]

            if template.startswith("morph_gen")
            else SHOT_PROCESSORS["default_disc"]
        ),
    )
    instruction_processor = INSTRUCTION_PROCESSORS.get(
        template, INSTRUCTION_PROCESSORS["default"]
    )

    shots = []
    for idx, shot_sample in enumerate(shot_samples):
        shot, answer = shot_processor(
            idx,
            shot_sample,
            template,
            language,
            shuffle_affixes=shuffle_affixes,
            fixed_shots=fixed_shots,
        )

        if isinstance(shot, list):
            chosen_answer = _choose_answer_based_on_template(_get_template_lang(template), idx)
            chosen_shot, _ = _choose_shot_based_on_answer(shot, answer, chosen_answer)
            shots.append(chosen_shot)
        else:
            shots.append(shot)

    shots_prompt = "\n\n".join(shots)

    final_shot, final_answer = shot_processor(
        len(shot_samples),
        sample,
        template,
        language,
        is_final=True,
        shuffle_affixes=shuffle_affixes,
    )

    if not isinstance(final_shot, list):
        final_shot = [final_shot]
        final_answer = [final_answer]
    
    eval_data = []
        
    for final_sh, final_ans in zip(final_shot, final_answer):
        instruction = instruction_processor(sample, template, language)

        if shots_prompt:
            prompt = f"{instruction}\n\n{shots_prompt}\n\n{final_sh}"
        else:
            prompt = f"{instruction}\n\n{final_sh}"

        eval_data.append(
            {
                "id": sample["id"],
                "root": sample["root"],
                "prefixes": sample.get("prefixes", []),
                "suffixes": sample.get("suffixes", []),
                "meta_prefixes": sample.get("meta_prefixes", []),
                "meta_suffixes": sample.get("meta_suffixes", []),
                "derivation": sample["derivation"],
                "prompt": prompt.strip(),
                "reference": final_ans,
                "template": template,
                "id_root": sample["id_root"] if "id_root" in sample else None,
                "id_derivation": (
                    sample["id_derivation"] if "id_derivation" in sample else None
                ),
                "sentence": sample.get("sentence"),
                "meaning": sample.get("meaning"),
                "negative_prefixes": sample.get("negative_prefixes", []),
                "negative_suffixes": sample.get("negative_suffixes", []),
                "negative_meta_prefixes": sample.get("negative_meta_prefixes", []),
                "negative_meta_suffixes": sample.get("negative_meta_suffixes", []),
            }
        )

    return eval_data

def prepare_sample_for_human_eval(sample, template, language, shuffle_affixes=True):
    eval_data = []
    eval_sample = {
        "sample_id": sample["id"],
        "root": sample["root"]
    }
    prefixes = sample.get("prefixes", []) or []
    suffixes = sample.get("suffixes", []) or []
    affixes = prefixes + suffixes
    negative_affixes = (sample.get("negative_prefixes", []) or []) + (sample.get("negative_suffixes", []) or [])

    if shuffle_affixes:
        affixes = random.sample(affixes, len(affixes))
        negative_affixes = random.sample(negative_affixes, len(negative_affixes))

    eval_sample["prefixes"] = prefixes
    eval_sample["suffixes"] = suffixes
    eval_sample["affixes"] = affixes

    if _is_ood_sample(sample):
        eval_sample["definition"] = sample["id_root"]

    if _is_sent_task(template):
        eval_sample["sentence"] = sample["sentence"]

    if "morph_gen" in template:
        eval_sample["answer"] = sample["derivation"]
        return [eval_sample]
    
    eval_data.append({
        **eval_sample,
        "derivation": sample["derivation"],
        "answer": "Yes"
    })

    for negative_option in sample["negative_options"][:4]:
        eval_data.append({
            **eval_sample,
            "affixes": negative_affixes if negative_affixes else affixes,
            "derivation": negative_option,
            "answer": "No"
        })

    return eval_data

def validate_eval_input_data(input_data):
    derivations = set()

    for sample in tqdm(input_data, desc="Validating eval input data"):
        assert "id" in sample, "Sample id is missing: {}".format(sample)
        assert "root" in sample, "Root is missing: {}".format(sample)
        assert "id_root" in sample, "ID root is missing: {}".format(sample)
        assert "ood_root" in sample, "OOD root is missing: {}".format(sample)
        assert "prefixes" in sample or "suffixes" in sample, "Prefixes or suffixes are missing: {}".format(sample)
        assert "derivation" in sample, "Derivation is missing: {}".format(sample)
        assert "positive_options" in sample, "Positive options are missing: {}".format(sample)
        assert "negative_options" in sample, "Negative options are missing: {}".format(sample)
        assert "sentence" in sample, "Sentence is missing: {}".format(sample)
        assert sample["root"].strip(), "Root is empty: {}".format(sample)
        assert sample["id_root"].strip(), "id root is empty: {}".format(sample)
        assert sample["ood_root"].strip(), "ood root is empty: {}".format(sample)
        assert sample["root"] == sample["id_root"] or sample["root"] == sample["ood_root"], "Root is not equal to id root or ood root: {}".format(sample)
        assert sample.get("prefixes") or sample.get("suffixes"), "Prefixes or suffixes are empty: {}".format(sample)
        assert sample["derivation"].strip(), "Derivation is empty: {}".format(sample)
        assert sample["positive_options"], "Positive options are empty: {}".format(sample)
        assert sample["negative_options"], "Negative options are empty: {}".format(sample)
        assert sample["sentence"].strip(), "Sentence is empty: {}".format(sample)
        assert sample["sentence"].count("___") == 1, "Sentence does not contain or contains more than one ___: {}".format(sample)
        assert set(sample["positive_options"]).intersection(set(sample["negative_options"])) == set(), "Positive and negative options overlap: {}".format(sample)
        assert sample["derivation"] not in derivations, "Derivation is repeated: {}".format(sample)
        derivations.add(sample["derivation"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, help="Path to eval data in json", required=True)
    parser.add_argument("-t", "--template", type=str, default="morph_gen_en", help="Template name")
    parser.add_argument("-n", "--num-shots", type=int, default=1)
    parser.add_argument(
        "-s",
        "--output-suffix",
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
        "-sp", "--shot-path", type=str, default=None, help="Path to shot data in json"
    )
    parser.add_argument(
        "-ns",
        "--no-shuffle",
        action="store_true",
        help="Do not shuffle the affix order",
    )
    parser.add_argument("-mal", "--max-affix-length", type=int, default=7, help="Max affix length to consider.")

    args = parser.parse_args()
    input_data = read_json(args.datapath)

    eval_data = []
    shot_samples = []
    shot_data = None
    fixed_shots = False

    validate_eval_input_data(input_data["data"])

    if args.shot_path is not None:
        shot_data = read_json(args.shot_path)
        fixed_shots = True

    for sample in tqdm(input_data["data"], desc="Preparing input_data for evaluation"):
        num_affixes = len(_get_affixes(sample))

        if num_affixes <= args.max_affix_length: 
            if "human" in args.template:
                eval_data.extend(
                    prepare_sample_for_human_eval(
                        sample,
                        template=args.template,
                        language=input_data["metadata"]["language"],
                        shuffle_affixes=not args.no_shuffle,
                    )
                )
            else:
                if shot_data:
                    shot_samples = [
                        shot
                        for shot in shot_data["data"]
                        if len(_get_affixes(shot)) == len(_get_affixes(sample))
                    ][: args.num_shots]
                else:
                    if sample.get("similar"):
                        shot_samples = sample["similar"]
                    else:
                        shot_samples = [
                            shot
                            for shot in input_data["data"]
                            if len(_get_affixes(shot)) == len(_get_affixes(sample))
                            and shot["id"] != sample["id"]
                        ]
                        # Order by the number of common affixes (prefer no overlap)
                        shot_samples = sorted(shot_samples, key=lambda x: len(set(_get_affixes(x)).intersection(set(_get_affixes(sample)))))
                        shot_samples = shot_samples[:args.num_shots]

                assert (
                    len(shot_samples) == args.num_shots
                ), f"Number of shots is not equal to {args.num_shots} for sample {sample['id']}"

                eval_data.extend(
                    prepare_sample_for_eval(
                        sample,
                        shot_samples,
                        template=args.template,
                        language=input_data["metadata"]["language"],
                        shuffle_affixes=not args.no_shuffle,
                        fixed_shots=fixed_shots,
                    )
                )

    datapath = pathlib.Path(args.datapath)
    output_dir = pathlib.Path(args.output_dir) if args.output_dir is not None else datapath.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    eval_data_path_stem = output_dir / f"{datapath.stem}_eval_{args.template}_s{args.num_shots}{args.output_suffix}"

    output_data = {
        "metadata": {
            "source": args.datapath,
            "template": args.template,
            "language": input_data["metadata"]["language"],
            "num_shots": args.num_shots,
            "output_suffix": args.output_suffix,
            "max_affix_length": args.max_affix_length,
            "shot_path": args.shot_path,
            "no_shuffle": args.no_shuffle,
            "output_dir": str(output_dir),
            "size": len(eval_data)
        },
        "data": eval_data
    }
    write_json(
        output_data, eval_data_path_stem.with_suffix(".json"), ensure_ascii=False
    )

    print(f"Output data saved to {eval_data_path_stem.with_suffix('.json')}")


if __name__ == "__main__":
    main()