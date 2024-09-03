from tqdm import tqdm

import json

with open("finnish_default_final_morph_affix1.json", "r") as f:
    json_data = json.load(f)
    sampled_negatives_data = json_data["data"]
    metadata = json_data["metadata"]

    output_json_lines = []
    for json_line in tqdm(sampled_negatives_data):
        id_root = json_line["id_root"]
        ood_root = json_line["ood_root"]
        prefixes = json_line["prefixes"]
        suffixes = json_line["suffixes"]
        negative_suffixes = json_line["negative_suffixes"]

        derivation = [*prefixes, id_root, *suffixes]
        negative_derivation = [*prefixes, id_root, *negative_suffixes]

        print(f"Positive: {derivation}, negative: {negative_derivation}")
        valid = input("Is the negative valid? (y/n): ")

        json_line["is_valid"] = valid
        output_json_lines.append(json_line)

    output_json = {"metadata": metadata, "data": output_json_lines}

    with open("finnish_default_final_morph_affix1_with_is_valid.json", "w") as f:
        json.dump(output_json, f, ensure_ascii=False, indent=None)
