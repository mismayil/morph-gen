import argparse
import pandas as pd
import pathlib
from tqdm import tqdm

from utils import read_json, write_json, find_files

def process_results(results_file, reference_file):
    results = pd.read_csv(results_file)
    reference = read_json(reference_file)

    if len(results) != len(reference["data"]):
        print(f"Results and reference files have different number of samples: {len(results)} vs {len(reference['data'])}")
        return
    
    reference_map = {}

    for sample in reference["data"]:
        if "derivation" in sample:
            reference_map[(sample["sample_id"], sample["derivation"])] = sample
        else:
            reference_map[sample["sample_id"]] = sample

    json_results = []

    for idx, row in tqdm(results.iterrows(), total=len(results), desc="Processing results"):
        sample_id = row["sample_id"]
        derivation = None
        ref_sample = None
        answer = None

        if "derivation" in row:
            derivation = row["derivation"]
        elif "Derivation" in row:
            derivation = row["Derivation"]

        if derivation is not None:
            derivation = derivation.lower()
            ref_sample = reference_map.get((sample_id, derivation))
        else:
            ref_sample = reference_map.get(sample_id)

        if ref_sample is None:
            print(f"Sample {sample_id} not found in reference")
            continue
        
        if "answer" in row:
            answer = row["answer"]
        elif "Answer" in row:
            answer = row["Answer"]

        sample = {
            **ref_sample,
            "id": ref_sample["sample_id"],
            "reference": ref_sample["answer"],
            "model_output": answer.split(",") if isinstance(answer, str) and "," in answer else answer,
            "template": reference["metadata"]["template"]
        }

        json_results.append(sample)
    
    outputs = {
        "metadata": {
            **reference["metadata"],
            "model": "human"
        },
        "metrics": {},
        "data": json_results
    }

    return outputs

def main():
    parser = argparse.ArgumentParser(description='Process human results')
    parser.add_argument("-r", "--results-path", help="Path to the results directory or file in csv format", required=True)
    parser.add_argument("-g", "--reference-path", help="Path to the reference directory or file in json format", required=True)

    args = parser.parse_args()

    results_files = []
    reference_files = []

    if args.results_path.endswith('.csv'):
        results_files.append(args.results_path)
    else:
        results_files = find_files(args.results_path, 'csv')
    
    if args.reference_path.endswith('.json'):
        reference_files.append(args.reference_path)
    else:
        reference_files = find_files(args.reference_path, 'json')
    
    res_ref_pairs = []

    if len(results_files) == 1 and len(reference_files) == 1:
        res_ref_pairs.append((results_files[0], reference_files[0]))
    else:
        for res_file in results_files:
            for ref_file in reference_files:
                ref_path = pathlib.Path(ref_file)
                res_path = pathlib.Path(res_file)
                if f"{ref_path.stem}_results" == res_path.stem:
                    res_ref_pairs.append((res_file, ref_file))
                    break
    
    for res_file, ref_file in res_ref_pairs:
        outputs = process_results(res_file, ref_file)
        res_path = pathlib.Path(res_file)
        outputs["metadata"]["source"] = [res_file, ref_file]
        outputs["metadata"]["output_dir"] = str(res_path.parent)

        write_json(outputs, res_path.with_suffix('.json'))

if __name__ == '__main__':
    main()