import argparse
from tqdm import tqdm
import pathlib
import re, csv

from utils import read_json, write_json, find_json_files

def tabulate_results(results_files):
    tab_results = []

    for results_file in tqdm(results_files, total=len(results_files), desc="Tabulating results"):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                task = "morph-gen" if "_morph_gen_" in results_file else "morph-disc"
                is_ood = "_nonce_" in results_file
                num_shots = int(re.search(r"_s(\d+)_", results_file).group(1))
                accuracy_metrics = results["metrics"]["accuracy_by_suffix_len"]
                faithful_metrics = results["metrics"]["faithfulness_by_suffix_len"]
                for suffix_len in accuracy_metrics.keys():
                    tab_results.append({
                        "task": task,
                        "is_ood": is_ood,
                        "num_shots": num_shots,
                        "num_suffixes": suffix_len,
                        "accuracy": accuracy_metrics[suffix_len],
                        "faithfulness": faithful_metrics[suffix_len]
                    })
        except Exception as e:
            print(results_file)
            raise e
    
    return tab_results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("-o", "--output-path", type=str, help="Path to save tabulated results", required=True)
    parser.add_argument("-f", "--output-format", type=str, choices=["csv", "json"], default="csv", help="Format to write results in.")

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_json_files(args.results_path))

    pathlib.Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)

    tab_results = tabulate_results(files_to_process)

    if args.output_format == "csv":
        with open(args.output_path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["task", "is_ood", "num_shots", "num_suffixes", "accuracy", "faithfulness"])
            writer.writeheader()
            writer.writerows(tab_results)
    elif args.output_format == "json":
        write_json(tab_results, args.output_path)
    else:
        raise ValueError(f"Invalid output format: {args.output_format}")

if __name__ == "__main__":
    main()