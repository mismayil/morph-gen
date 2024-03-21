import argparse
from tqdm import tqdm
import pathlib
import re, csv

from utils import read_json, write_json, find_json_files

def tabulate_results(results_files):
    tab_results = []
    tab_results_by_unigram_freq = []
    tab_results_by_suffix_freq = []
    tab_results_by_meta_suffix_freq = []

    for results_file in tqdm(results_files, total=len(results_files), desc="Tabulating results"):
        results = read_json(results_file)
        
        try:
            if "data" in results:
                task = "morph-gen" if "_morph_gen_" in results_file else "morph-disc"
                is_ood = "_nonce_" in results_file
                num_shots = int(re.search(r"_s(\d+)_", results_file).group(1))
                
                accuracy_metrics = results["metrics"]["accuracy_by_suffix_len"]
                faithful_metrics = results["metrics"]["faithfulness_by_suffix_len"]
                
                accuracy_by_unigram_freq = results["metrics"].get("accuracy_by_unigram_freq")
                faithful_by_unigram_freq = results["metrics"].get("faithfulness_by_unigram_freq")
                num_samples_by_unigram_freq = results["metrics"].get("num_samples_by_unigram_freq")

                accuracy_by_suffix_freq = results["metrics"].get("accuracy_by_suffix_freq")
                faithful_by_suffix_freq = results["metrics"].get("faithfulness_by_suffix_freq")
                num_samples_by_suffix_freq = results["metrics"].get("num_samples_by_suffix_freq")

                accuracy_by_meta_suffix_freq = results["metrics"].get("accuracy_by_meta_suffix_freq")
                faithful_by_meta_suffix_freq = results["metrics"].get("faithfulness_by_meta_suffix_freq")
                num_samples_by_meta_suffix_freq = results["metrics"].get("num_samples_by_meta_suffix_freq")

                def _add_by_freq_results(results_by_freq, accuracy_by_freq, faithful_by_freq, num_samples_by_freq):
                    for freq_bin, freq_res in num_samples_by_freq.items():
                        for suffix_len, num_samples_by_slen in freq_res.items():
                            results_by_freq.append({
                                "task": task,
                                "is_ood": is_ood,
                                "num_shots": num_shots,
                                "freq_bin": freq_bin,
                                "num_suffixes": suffix_len,
                                "num_samples": num_samples_by_slen,
                                "accuracy": accuracy_by_freq[freq_bin],
                                "faithfulness": faithful_by_freq[freq_bin]
                            })

                for suffix_len in accuracy_metrics.keys():
                    tab_results.append({
                        "task": task,
                        "is_ood": is_ood,
                        "num_shots": num_shots,
                        "num_suffixes": suffix_len,
                        "accuracy": accuracy_metrics[suffix_len],
                        "faithfulness": faithful_metrics[suffix_len]
                    })
                
                if accuracy_by_unigram_freq:
                    _add_by_freq_results(tab_results_by_unigram_freq, accuracy_by_unigram_freq, faithful_by_unigram_freq, num_samples_by_unigram_freq)
                
                if accuracy_by_suffix_freq:
                    _add_by_freq_results(tab_results_by_suffix_freq, accuracy_by_suffix_freq, faithful_by_suffix_freq, num_samples_by_suffix_freq)
                
                if accuracy_by_meta_suffix_freq:
                    _add_by_freq_results(tab_results_by_meta_suffix_freq, accuracy_by_meta_suffix_freq, faithful_by_meta_suffix_freq, num_samples_by_meta_suffix_freq)

        except Exception as e:
            print(results_file)
            raise e
    
    return {
        "tab_results": tab_results, 
        "tab_results_by_unigram_freq": tab_results_by_unigram_freq, 
        "tab_results_by_suffix_freq": tab_results_by_suffix_freq, 
        "tab_results_by_meta_suffix_freq": tab_results_by_meta_suffix_freq
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results-path", type=str, help="Path to evaluation results file in json or directory", required=True)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory to save tabulated results")
    parser.add_argument("-f", "--output-format", type=str, choices=["csv", "json"], default="csv", help="Format to write results in.")

    args = parser.parse_args()

    files_to_process = []

    results_path = pathlib.Path(args.results_path)

    if results_path.is_file():
        files_to_process.append(args.results_path)
    else:
        files_to_process.extend(find_json_files(args.results_path))

    if not args.output_dir:
        if results_path.is_file():
            output_dir = results_path.parent
        else:
            output_dir = results_path
    else:
        output_dir = pathlib.Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    results_map = tabulate_results(files_to_process)

    for result_key, results in results_map.items():
        if results:
            if args.output_format == "csv":
                output_path = output_dir / f"{result_key}.csv"
                with open(output_path, "w") as f:
                    writer = csv.DictWriter(f, fieldnames=results[0].keys())
                    writer.writeheader()
                    writer.writerows(results)
            elif args.output_format == "json":
                output_path = output_dir / f"{result_key}.json"
                write_json(results, output_path)
            else:
                raise ValueError(f"Invalid output format: {args.output_format}")

if __name__ == "__main__":
    main()