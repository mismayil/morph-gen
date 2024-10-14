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

def export_main_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting main results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            export_data[model]["gen-acc"]["OOD"][num_shots] = _format_metric(metric)
                        else:
                            export_data[model]["gen-acc"]["ID"][num_shots] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            export_data[model]["disc-f1"]["OOD"][num_shots] = _format_metric(metric)
                        else:
                            export_data[model]["disc-f1"]["ID"][num_shots] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            export_data[model]["disc-coh"]["OOD"][num_shots] = _format_metric(metric)
                        else:
                            export_data[model]["disc-coh"]["ID"][num_shots] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_affix_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by affix results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy_by_affix_len"]
                        if _is_ood(results):
                            export_data[model]["gen-acc"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            export_data[model]["gen-acc"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1_by_affix_len"]
                        if _is_ood(results):
                            export_data[model]["disc-f1"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            export_data[model]["disc-f1"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        
                        metric = results["metrics"]["coherence_by_affix_len"]
                        if _is_ood(results):
                            export_data[model]["disc-coh"]["OOD"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            export_data[model]["disc-coh"]["ID"][num_shots] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_context_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by context results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    sent_task = "sent" in template
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][sent_task] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][sent_task] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][sent_task] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][sent_task] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][sent_task] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][sent_task] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_lang_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by lang results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    lang = template.split("_")[-1]
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][lang] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][lang] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][lang] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][lang] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][lang] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][lang] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_comp_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by composition results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    tok_aligned = "tok_aligned" in result_file
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy_by_affix_len"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1_by_affix_len"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        
                        metric = results["metrics"]["coherence_by_affix_len"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][tok_aligned] = [_format_metric(metric) for affix_len, metric in sorted(metric.items(), key=lambda x: int(x[0]))]
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_cot_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by cot results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    cot = "cot" in template
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][cot] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][cot] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][cot] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][cot] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][cot] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][cot] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_order_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by order results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    correct_order = "no_shuffle" in result_file
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][correct_order] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][correct_order] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][correct_order] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][correct_order] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][correct_order] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][correct_order] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def export_by_negsel_results(results_dirs):
    export_data = {}

    for results_dir in results_dirs:
        result_files = find_files(results_dir, "json")

        for result_file in tqdm(result_files, desc="Exporting by order results"):
            try:
                results = read_json(result_file)
                
                if "metadata" in results and "metrics" in results:
                    model = results["metadata"]["model"]
                    if model not in export_data:
                        export_data[model] = {
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
                    template = _get_template(results)
                    num_shots = _get_num_shots(results)
                    negsel = "no_dv" if "no_dv_neg" in result_file else "random" if "random_neg" in result_file else "lev"
                    
                    if "morph_gen" in template:
                        metric = results["metrics"]["accuracy"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["gen-acc"]["OOD"]:
                                export_data[model]["gen-acc"]["OOD"][num_shots] = {}
                            export_data[model]["gen-acc"]["OOD"][num_shots][negsel] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["gen-acc"]["ID"]:
                                export_data[model]["gen-acc"]["ID"][num_shots] = {}
                            export_data[model]["gen-acc"]["ID"][num_shots][negsel] = _format_metric(metric)
                    elif "morph_disc" in template:
                        metric = results["metrics"]["f1"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-f1"]["OOD"]:
                                export_data[model]["disc-f1"]["OOD"][num_shots] = {}
                            export_data[model]["disc-f1"]["OOD"][num_shots][negsel] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-f1"]["ID"]:
                                export_data[model]["disc-f1"]["ID"][num_shots] = {}
                            export_data[model]["disc-f1"]["ID"][num_shots][negsel] = _format_metric(metric)
                        
                        metric = results["metrics"]["coherence"]
                        if _is_ood(results):
                            if num_shots not in export_data[model]["disc-coh"]["OOD"]:
                                export_data[model]["disc-coh"]["OOD"][num_shots] = {}
                            export_data[model]["disc-coh"]["OOD"][num_shots][negsel] = _format_metric(metric)
                        else:
                            if num_shots not in export_data[model]["disc-coh"]["ID"]:
                                export_data[model]["disc-coh"]["ID"][num_shots] = {}
                            export_data[model]["disc-coh"]["ID"][num_shots][negsel] = _format_metric(metric)
            except Exception as e:
                print(f"Error exporting {result_file}: {e}")
    
    return export_data

def _get_ordered_shot_results(shot_results):
    ordered_res = sorted(shot_results.items(), key=lambda x: int(x[0]))
    return [res[1] for res in ordered_res]

def _get_lang_ordered_shot_results(shot_results):
    lang_order = ["en", "tr", "fi"]
    ordered_res = sorted(shot_results.items(), key=lambda x: lang_order.index(x[0]))
    return [res[1] for res in ordered_res]

def _get_negsel_ordered_shot_results(shot_results):
    lang_order = ["random", "lev", "no_dv"]
    ordered_res = sorted(shot_results.items(), key=lambda x: lang_order.index(x[0]))
    return [res[1] for res in ordered_res]

def export_to_latex(export_data, output_path, export_type="main"):
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if export_type == "main":
        with open(output_path, "w") as f:
            for model, datapoint in export_data.items():
                gen_acc_id = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["ID"]))
                gen_acc_ood = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["OOD"]))
                disc_f1_id = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["ID"]))
                disc_f1_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["OOD"]))
                disc_coh_id = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["ID"]))
                disc_coh_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["OOD"]))
                f.write(f"\\textbf{{{model}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_affix":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["gen-acc"]["ID"].keys()))
        for task in ["gen-acc", "disc-f1", "disc-coh"]:
            for num_shots in num_shots_lst:
                local_output_path = output_path.parent / f"{output_path.stem}_{task}_s{num_shots}.tex"
                with open(local_output_path, "w") as f:
                    for model, datapoint in export_data.items():
                        if num_shots in datapoint[task]["ID"]:
                            task_id = datapoint[task]["ID"][num_shots]
                            task_ood = datapoint[task]["OOD"][num_shots]
                            task_id_ood = " & ".join([f"{i} / {o}" for i, o in zip(task_id, task_ood)])
                            f.write(f"\\textbf{{{model}}} & {task_id_ood} \\\\\n")
    elif export_type == "by_lang":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["gen-acc"]["ID"].keys()))
        for num_shots in num_shots_lst:
            local_output_path = output_path.parent / f"{output_path.stem}_s{num_shots}.tex"
            with open(local_output_path, "w") as f:
                for model, datapoint in export_data.items():
                    if num_shots in datapoint["gen-acc"]["ID"]:
                        gen_acc_id = " / ".join(_get_lang_ordered_shot_results(datapoint["gen-acc"]["ID"][num_shots]))
                        gen_acc_ood = " / ".join(_get_lang_ordered_shot_results(datapoint["gen-acc"]["OOD"][num_shots]))
                        disc_f1_id = " / ".join(_get_lang_ordered_shot_results(datapoint["disc-f1"]["ID"][num_shots]))
                        disc_f1_ood = " / ".join(_get_lang_ordered_shot_results(datapoint["disc-f1"]["OOD"][num_shots]))
                        disc_coh_id = " / ".join(_get_lang_ordered_shot_results(datapoint["disc-coh"]["ID"][num_shots]))
                        disc_coh_ood = " / ".join(_get_lang_ordered_shot_results(datapoint["disc-coh"]["OOD"][num_shots]))
                        f.write(f"\\textbf{{{model}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_context":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["gen-acc"]["ID"].keys()))
        for num_shots in num_shots_lst:
            local_output_path = output_path.parent / f"{output_path.stem}_s{num_shots}.tex"
            with open(local_output_path, "w") as f:
                for model, datapoint in export_data.items():
                    if num_shots in datapoint["gen-acc"]["ID"]:
                        gen_acc_id = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["ID"][num_shots]))
                        gen_acc_ood = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["OOD"][num_shots]))
                        disc_f1_id = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["ID"][num_shots]))
                        disc_f1_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["OOD"][num_shots]))
                        disc_coh_id = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["ID"][num_shots]))
                        disc_coh_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["OOD"][num_shots]))
                        f.write(f"\\textbf{{{model}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_comp":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["gen-acc"]["ID"].keys()))
        for task in ["gen-acc", "disc-f1", "disc-coh"]:
            for num_shots in num_shots_lst:
                local_output_path = output_path.parent / f"{output_path.stem}_{task}_s{num_shots}_id.tex"
                with open(local_output_path, "w") as f:
                    for model, datapoint in export_data.items():
                        if num_shots in datapoint[task]["ID"]:
                            task_id_morph_aligned = datapoint[task]["ID"][num_shots][False]
                            task_id_tok_aligned = datapoint[task]["ID"][num_shots][True]
                            task_by_comp = " & ".join([f"{i} / {o}" for i, o in zip(task_id_morph_aligned, task_id_tok_aligned)])
                            f.write(f"\\textbf{{{model}}} & {task_by_comp} \\\\\n")
    elif export_type == "by_cot":
        local_output_path = output_path.parent / f"{output_path.stem}_s505.tex"
        with open(local_output_path, "w") as f:
            for model, datapoint in export_data.items():
                gen_acc_id = " / ".join([datapoint["gen-acc"]["ID"][5][False], datapoint["gen-acc"]["ID"][0][True], datapoint["gen-acc"]["ID"][5][True]])
                gen_acc_ood = " / ".join([datapoint["gen-acc"]["OOD"][5][False], datapoint["gen-acc"]["OOD"][0][True], datapoint["gen-acc"]["OOD"][5][True]])
                disc_f1_id = " / ".join([datapoint["disc-f1"]["ID"][5][False], datapoint["disc-f1"]["ID"][0][True], datapoint["disc-f1"]["ID"][5][True]])
                disc_f1_ood = " / ".join([datapoint["disc-f1"]["OOD"][5][False], datapoint["disc-f1"]["OOD"][0][True], datapoint["disc-f1"]["OOD"][5][True]])
                disc_coh_id = " / ".join([datapoint["disc-coh"]["ID"][5][False], datapoint["disc-coh"]["ID"][0][True], datapoint["disc-coh"]["ID"][5][True]])
                disc_coh_ood = " / ".join([datapoint["disc-coh"]["OOD"][5][False], datapoint["disc-coh"]["OOD"][0][True], datapoint["disc-coh"]["OOD"][5][True]])
                f.write(f"\\textbf{{{model}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_order":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["gen-acc"]["ID"].keys()))
        for num_shots in num_shots_lst:
            local_output_path = output_path.parent / f"{output_path.stem}_s{num_shots}.tex"
            with open(local_output_path, "w") as f:
                for model, datapoint in export_data.items():
                    if num_shots in datapoint["gen-acc"]["ID"]:
                        gen_acc_id = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["ID"][num_shots]))
                        gen_acc_ood = " / ".join(_get_ordered_shot_results(datapoint["gen-acc"]["OOD"][num_shots]))
                        disc_f1_id = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["ID"][num_shots]))
                        disc_f1_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-f1"]["OOD"][num_shots]))
                        disc_coh_id = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["ID"][num_shots]))
                        disc_coh_ood = " / ".join(_get_ordered_shot_results(datapoint["disc-coh"]["OOD"][num_shots]))
                        f.write(f"\\textbf{{{model}}} & {gen_acc_id} & {gen_acc_ood} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    elif export_type == "by_negsel":
        num_shots_lst = sorted(list(export_data[list(export_data.keys())[0]]["disc-f1"]["ID"].keys()))
        for num_shots in num_shots_lst:
            local_output_path = output_path.parent / f"{output_path.stem}_s{num_shots}.tex"
            with open(local_output_path, "w") as f:
                for model, datapoint in export_data.items():
                    if num_shots in datapoint["gen-acc"]["ID"]:
                        disc_f1_id = " / ".join(_get_negsel_ordered_shot_results(datapoint["disc-f1"]["ID"][num_shots]))
                        disc_f1_ood = " / ".join(_get_negsel_ordered_shot_results(datapoint["disc-f1"]["OOD"][num_shots]))
                        disc_coh_id = " / ".join(_get_negsel_ordered_shot_results(datapoint["disc-coh"]["ID"][num_shots]))
                        disc_coh_ood = " / ".join(_get_negsel_ordered_shot_results(datapoint["disc-coh"]["OOD"][num_shots]))
                        f.write(f"\\textbf{{{model}}} & {disc_f1_id} & {disc_f1_ood} & {disc_coh_id} & {disc_coh_ood} \\\\\n")
    else:
        raise ValueError("Invalid export type")

    print(f"Results exported to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Export results")
    parser.add_argument("-r", "--results-dirs", type=str, nargs="+", help="Results directories", required=True)
    parser.add_argument("-o", "--output-path", type=str, help="Output path", required=True)
    parser.add_argument("-f", "--format", type=str, choices=["latex"], default="latex", help="Output format")
    parser.add_argument("-t", "--export-type", type=str, choices=["main", "by_affix", "by_lang", "by_context", "by_comp", "by_cot", "by_order", "by_negsel"], default="main", help="Export type")

    args = parser.parse_args()

    export_data = {}

    if args.export_type == "main":
        export_data = export_main_results(args.results_dirs)
    elif args.export_type == "by_affix":
        export_data = export_by_affix_results(args.results_dirs)
    elif args.export_type == "by_context":
        export_data = export_by_context_results(args.results_dirs)
    elif args.export_type == "by_lang":
        export_data = export_by_lang_results(args.results_dirs)
    elif args.export_type == "by_comp":
        export_data = export_by_comp_results(args.results_dirs)
    elif args.export_type == "by_cot":
        export_data = export_by_cot_results(args.results_dirs)
    elif args.export_type == "by_order":
        export_data = export_by_order_results(args.results_dirs)
    elif args.export_type == "by_negsel":
        export_data = export_by_negsel_results(args.results_dirs)
    else:
        raise ValueError("Invalid export type")
    
    if args.format == "latex":
        export_to_latex(export_data, args.output_path, args.export_type)
    else:
        raise ValueError("Invalid format")

if __name__ == '__main__':
    main()