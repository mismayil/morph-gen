import argparse
import pathlib
import re
from tqdm import tqdm
from collections import defaultdict

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

def export_main_results(results_dir):
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

    for result_file in tqdm(result_files, desc="Exporting main results"):
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

def export_by_affix_results(results_dir):
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

    for result_file in tqdm(result_files, desc="Exporting by affix results"):
        try:
            results = read_json(result_file)
            
            if "metadata" in results and "metrics" in results:
                model = results["metadata"]["model"]
                template = _get_template(results)
                num_shots = _get_num_shots(results)
                
                if "morph_gen" in template:
                    metric = results["metrics"]["accuracy_by_affix_len"]
                    if _is_ood(results):
                        export_data["gen-acc"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    else:
                        export_data["gen-acc"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                elif "morph_disc" in template:
                    metric = results["metrics"]["f1_by_affix_len"]
                    if _is_ood(results):
                        export_data["disc-f1"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    else:
                        export_data["disc-f1"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    
                    metric = results["metrics"]["coherence_by_affix_len"]
                    if _is_ood(results):
                        export_data["disc-coh"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    else:
                        export_data["disc-coh"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                
                export_data["model"] = model
        except Exception as e:
            print(f"Error exporting {result_file}: {e}")
    
    return export_data

def _get_ordered_shot_results(shot_results):
    ordered_res = sorted(shot_results.items(), key=lambda x: int(x[0]))
    return [res[1] for res in ordered_res]

def export_to_latex(export_data, output_path, export_type="main"):
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if export_type == "main":
        with open(output_path, "w") as f:
            for datapoint in export_data:
                gen_acc_id = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["ID"]))
                gen_acc_ood = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["OOD"]))
                disc_f1_id = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["ID"]))
                disc_f1_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["OOD"]))
                disc_coh_id = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["ID"]))
                disc_coh_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["OOD"]))
                f.write(f"\\textbf{{{datapoint['model']}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_affix":
        num_shots_lst = sorted(list(export_data[0]["gen-acc"]["ID"].keys()))
        for task in ["gen-acc", "disc-f1", "disc-coh"]:
            for num_shots in num_shots_lst:
                local_output_path = output_path.parent / f"{output_path.stem}_{task}_s{num_shots}.tex"
                with open(local_output_path, "w") as f:
                    for datapoint in export_data:
                        if num_shots in datapoint[task]["ID"]:
                            task_id = datapoint[task]["ID"][num_shots]
                            task_ood = datapoint[task]["OOD"][num_shots]
                            task_id_ood = " & ".join([f"{i} / {o}" for i, o in zip(task_id, task_ood)])
                            f.write(f"\\textbf{{{datapoint['model']}}} & {task_id_ood} \\\\\n")
    else:
        raise ValueError("Invalid export type")

    print(f"Results exported to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Export results")
    parser.add_argument("-r", "--results-dirs", type=str, nargs="+", help="Results directories", required=True)
    parser.add_argument("-o", "--output-path", type=str, help="Output path", required=True)
    parser.add_argument("-f", "--format", type=str, choices=["latex"], default="latex", help="Output format")
    parser.add_argument("-t", "--export-type", type=str, choices=["main", "by_affix"], default="main", help="Export type")

    args = parser.parse_args()

    export_data = []

    for result_dir in args.results_dirs:
        if args.export_type == "main":
            export_data.append(export_main_results(result_dir))
        elif args.export_type == "by_affix":
            export_data.append(export_by_affix_results(result_dir))
        else:
            raise ValueError("Invalid export type")
    
    if args.format == "latex":
        export_to_latex(export_data, args.output_path, args.export_type)
    else:
        raise ValueError("Invalid format")

if __name__ == '__main__':
    main()