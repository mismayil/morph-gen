import argparse
import pathlib
import re
from tqdm import tqdm

from utils import read_json, find_files

def _is_ood(results):
    return results["data"][0]["id"].endswith("ood")

def _format_metric(metric):
    return f"{metric*100:.1f}"

def _get_template(results):
    if "template" in results["metadata"]:
        return results["metadata"]["template"]
    
    return results["data"][0]["template"]

def _get_num_shots(results):
    if "num_shots" in results["metadata"]:
        return results["metadata"]["num_shots"]
    
    datapath = pathlib.Path(results["metadata"]["datapath"])
    match = re.search(r"_s(\d+)", datapath.stem)
    if match:
        return int(match.group()[-1])

def export_results(results_dir):
    export_data = {
        "model": "",
        "gen-acc": {
            "ID": {}, "OOD": {}
        },
        "disc-f1": {
            "ID": {}, "OOD": {}
        },
        "disc-coh": {
            "ID": {}, "OOD": {}
        }
    }
    result_files = find_files(results_dir, "json")

    for result_file in tqdm(result_files, desc="Exporting results"):
        try:
            results = read_json(result_file)
            
            if "metadata" in results and "metrics" in results:
                model = results["metadata"]["model"]
                template = _get_template(results)
                num_shots = _get_num_shots(results)
                
                if "morph_gen" in template:
                    metric = results["metrics"]["accuracy"]
                    if _is_ood(results):
                        export_data["gen-acc"]["OOD"][num_shots] = _format_metric(metric)
                    else:
                        export_data["gen-acc"]["ID"][num_shots] = _format_metric(metric)
                elif "morph_disc" in template:
                    metric = results["metrics"]["f1"]
                    if _is_ood(results):
                        export_data["disc-f1"]["OOD"][num_shots] = _format_metric(metric)
                    else:
                        export_data["disc-f1"]["ID"][num_shots] = _format_metric(metric)
                    
                    metric = results["metrics"]["coherence"]
                    if _is_ood(results):
                        export_data["disc-coh"]["OOD"][num_shots] = _format_metric(metric)
                    else:
                        export_data["disc-coh"]["ID"][num_shots] = _format_metric(metric)
                
                export_data["model"] = model
        except Exception as e:
            print(f"Error exporting {result_file}: {e}")
    
    return export_data

def _get_ordered_shot_results(shot_results):
    ordered_res = sorted(shot_results.items(), key=lambda x: int(x[0]))
    return [res[1] for res in ordered_res]

def export_to_latex(export_data, output_path):
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for datapoint in export_data:
            gen_acc_id = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["ID"]))
            gen_acc_ood = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["OOD"]))
            disc_f1_id = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["ID"]))
            disc_f1_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["OOD"]))
            disc_coh_id = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["ID"]))
            disc_coh_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["OOD"]))
            f.write(f"\\textbf{{{datapoint['model']}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    
    print(f"Results exported to {output_path}")

def export_to_csv(export_data, output_path):
    pass

def main():
    parser = argparse.ArgumentParser(description="Export results")
    parser.add_argument("-r", "--results-dirs", type=str, nargs="+", help="Results directories", required=True)
    parser.add_argument("-o", "--output-path", type=str, help="Output path", required=True)
    parser.add_argument("-f", "--format", type=str, choices=["latex", "csv"], default="latex", help="Output format")

    args = parser.parse_args()

    export_data = []

    for result_dir in args.results_dirs:
        export_data.append(export_results(result_dir))
    
    if args.format == "latex":
        export_to_latex(export_data, args.output_path)
    elif args.format == "csv":
        export_to_csv(export_data, args.output_path)
    else:
        raise ValueError("Invalid format")

if __name__ == '__main__':
    main()