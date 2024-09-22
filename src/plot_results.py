import argparse
import pathlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

METRICS = ["faithfulness", "accuracy", "f1", "coherence"]

ABBR_METRICS = {
    "faithfulness": "faith",
    "accuracy": "acc",
    "f1": "f1",
    "coherence": "coh"
}

TASK_TITLE_MAP = {
    "morph-disc": "Discriminative Task",
    "morph-gen": "Generative Task"
}

FIG_SIZE = (40, 40)
XLABEL_SIZE = 80
YLABEL_SIZE = 80
TITLE_SIZE = 100
TICK_SIZE = 60
LEGEND_TITLE_SIZE = 70
LEGEND_SIZE = 60
Y_LIM_MIN = 0.0
Y_LIM_MAX = 1.0

def _get_language(tab_results):
    if "language" in tab_results.columns:
        return tab_results["language"].values[0]
    return "tr"

def _get_template(tab_results):
    if "template" in tab_results.columns:
        return tab_results["template"].values[0].split("_")[-1]
    return "en"

def _get_model(tab_results):
    if "model" in tab_results.columns:
        return tab_results["model"].values[0]
    return "gpt-4"

def plot_results(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", is_ood=False, max_affix_length=10):
    results = tab_results_lst[0]
    language = _get_language(results)
    template = _get_template(results)
    model = _get_model(results)

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{language}_{template}_{model}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = results.query(f"is_ood == {is_ood} & task == '{task}' & num_affixes <= {max_affix_length}")
    
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, ax = plt.subplots(figsize=FIG_SIZE)
        # ax.set_title(f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, dist={'OOD' if is_ood else 'ID'}, task={task}]")
        ax.set_title(f"{TASK_TITLE_MAP[task]} - {metric.capitalize()}")
        ax.set_xlabel("Number of affixes", size=XLABEL_SIZE)
        ax.set_ylabel(metric.capitalize(), size=YLABEL_SIZE)
        ax.tick_params(axis='x', labelsize=TICK_SIZE)
        ax.tick_params(axis='y', labelsize=TICK_SIZE)
        ax.set_ylim(Y_LIM_MIN, Y_LIM_MAX)
        ax.title.set_size(TITLE_SIZE)
        sns.barplot(data=results, x="num_affixes", y=metric, hue="num_shots", ax=ax, errorbar=None)
        
        # random baseline
        if f"random_{metric}" in results.columns:
            sns.barplot(data=results, x="num_affixes", y=f"random_{metric}", hue="num_shots", ax=ax, errorbar=None, legend=False)
        
        # majority baseline
        if f"majority_{metric}" in results.columns:
            sns.barplot(data=results, x="num_affixes", y=f"majority_{metric}", hue="num_shots", ax=ax, errorbar=None, legend=False)

        ax.legend(title="Number of shots", title_fontsize=LEGEND_TITLE_SIZE, fontsize=LEGEND_SIZE)
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_{'ood' if is_ood else 'id'}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)

def plot_results_by_freq(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", is_ood=False, keyword="unigram", max_affix_length=10):
    results = tab_results_lst[0]
    language = _get_language(results)
    template = _get_template(results)
    model = _get_model(results)

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{language}_{template}_{model}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = results.query(f"is_ood == {is_ood} & task == '{task}' & num_suffixes <= {max_affix_length}")
    
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, axes = plt.subplots(figsize=(16, 8), nrows=1, ncols=2)
        
        axes[0].set_title(f"{metric.capitalize()} by frequency \n [lang={language}, temp={template}, model={model}] \n [dist={'OOD' if is_ood else 'ID'}, task={task}]")
        axes[0].set_xlabel(f"{keyword.capitalize()} frequency")
        axes[0].set_ylabel(metric.capitalize())
        axes[0].title.set_size(20)
        sns.barplot(data=results, x="freq_bin", y=metric, hue="num_shots", ax=axes[0])

        axes[1].set_title(f"Number of samples by suffix length and frequency \n [lang={language}, temp={template}, model={model}] \n [dist={'OOD' if is_ood else 'ID'}, task={task}]")
        axes[1].set_xlabel(f"{keyword.capitalize()} frequency")
        axes[1].set_ylabel("Number of samples")
        axes[1].title.set_size(20)
        sns.barplot(data=results, x="freq_bin", y="num_samples", hue="num_suffixes", ax=axes[1])

        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_by_{keyword.replace(' ', '_')}_freq_{task}_{'ood' if is_ood else 'id'}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)

def plot_results_id_vs_ood(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", max_affix_length=10, num_shots=5):
    results = tab_results_lst[0]
    language = _get_language(results)
    template = _get_template(results)
    model = _get_model(results)

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{language}_{template}_{model}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = results.query(f"task == '{task}' & num_affixes <= {max_affix_length} & num_shots == {num_shots}").copy()
    
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, ax = plt.subplots(figsize=FIG_SIZE)
        # ax.set_title(f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, num_shots={num_shots}, task={task}]")
        ax.set_title(f"{TASK_TITLE_MAP[task]} - {metric.capitalize()}")
        ax.set_xlabel("Number of affixes", size=XLABEL_SIZE)
        ax.set_ylabel(metric.capitalize(), size=YLABEL_SIZE)
        ax.tick_params(axis='x', labelsize=TICK_SIZE)
        ax.tick_params(axis='y', labelsize=TICK_SIZE)
        ax.set_ylim(Y_LIM_MIN, Y_LIM_MAX)
        ax.title.set_size(TITLE_SIZE)
        results["dist"] = results["is_ood"].replace({False: "ID", True: "OOD"})
        sns.barplot(data=results, x="num_affixes", y=metric, hue="dist", hue_order=["ID", "OOD"], ax=ax, errorbar=None, palette="rocket")

        # random baseline
        if f"random_{metric}" in results.columns:
            sns.barplot(data=results, x="num_affixes", y=f"random_{metric}", hue="dist", hue_order=["ID", "OOD"], ax=ax, errorbar=None, palette="rocket", legend=False)
        
        # majority baseline
        if f"majority_{metric}" in results.columns:
            sns.barplot(data=results, x="num_affixes", y=f"majority_{metric}", hue="dist", hue_order=["ID", "OOD"], ax=ax, errorbar=None, palette="rocket", legend=False)

        ax.legend(title="Test Distribution", title_fontsize=LEGEND_TITLE_SIZE, fontsize=LEGEND_SIZE)
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_s{num_shots}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)

def plot_results_overall(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", max_affix_length=10):
    results = tab_results_lst[0]
    language = _get_language(results)
    template = _get_template(results)
    model = _get_model(results)

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{language}_{template}_{model}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = results.query(f"task == '{task}' & num_affixes <= {max_affix_length}").copy()
    
    if len(results) > 0 and any(results[metric] > 0):
        agg_dict = {"accuracy": "mean", "f1": "mean", "coherence": "mean", "faithfulness": "mean"}

        if f"random_{metric}" in results.columns:
            agg_dict[f"random_{metric}"] = "mean"
        
        if f"majority_{metric}" in results.columns:
            agg_dict[f"majority_{metric}"] = "mean"

        overall_results = results.groupby(["task", "is_ood", "num_shots"]).agg(agg_dict).reset_index()
        plt.ioff()
        fig, ax = plt.subplots(figsize=FIG_SIZE)
        # ax.set_title(f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, task={task}]")
        ax.set_title(f"{TASK_TITLE_MAP[task]} - {metric.capitalize()}")
        ax.set_xlabel("Test Distribution", size=XLABEL_SIZE)
        ax.set_ylabel(metric.capitalize(), size=YLABEL_SIZE)
        ax.tick_params(axis='x', labelsize=TICK_SIZE)
        ax.tick_params(axis='y', labelsize=TICK_SIZE)
        ax.set_ylim(Y_LIM_MIN, Y_LIM_MAX)
        ax.title.set_size(TITLE_SIZE)
        overall_results["dist"] = overall_results["is_ood"].replace({False: "ID", True: "OOD"})
        sns.barplot(data=overall_results, x="dist", y=metric, hue="num_shots", ax=ax, errorbar=None)

        # random baseline
        if f"random_{metric}" in results.columns:
            sns.barplot(data=overall_results, x="dist", y=f"random_{metric}", hue="num_shots", ax=ax, errorbar=None, legend=False)
        
        # majority baseline
        if f"majority_{metric}" in results.columns:
            sns.barplot(data=overall_results, x="dist", y=f"majority_{metric}", hue="num_shots", ax=ax, errorbar=None, legend=False)

        ax.legend(title="Number of shots", title_fontsize=LEGEND_TITLE_SIZE, fontsize=LEGEND_SIZE)
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)

def plot_results_by_lang(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", max_affix_length=10, num_shots=5):
    templates = [_get_template(tab_results) for tab_results in tab_results_lst]
    models = [_get_model(tab_results) for tab_results in tab_results_lst]
    languages = [_get_language(tab_results) for tab_results in tab_results_lst]

    assert len(set(languages)) == 1, "All tabulated results must be for the same language."
    assert len(set(templates)) == 1, "All tabulated results must be for the same template."
    assert len(set(models)) == 1, "All tabulated results must be for the same model."

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{languages[0]}_{templates[0]}_{models[0]}"
    output_dir.mkdir(parents=True, exist_ok=True)

    for tab_results, template in zip(tab_results_lst, templates):
        tab_results["template"] = template

    merged_results = pd.concat(tab_results_lst)

    results = merged_results.query(f"task == '{task}' & num_affixes <= {max_affix_length} & num_shots == {num_shots}")
    overall_results = results.groupby(["is_ood", "template"]).agg({"accuracy": "mean", "f1": "mean", "coherence": "mean", "faithfulness": "mean"}).reset_index().copy()
    overall_results["dist"] = overall_results["is_ood"].replace({False: "ID", True: "OOD"})

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.set_title(f"{TASK_TITLE_MAP[task]} - {metric.capitalize()}")
    ax.set_xlabel("Test Distribution", size=XLABEL_SIZE)
    ax.set_ylabel(metric.capitalize(), size=YLABEL_SIZE)
    ax.tick_params(axis='x', labelsize=TICK_SIZE)
    ax.tick_params(axis='y', labelsize=TICK_SIZE)
    ax.set_ylim(Y_LIM_MIN, Y_LIM_MAX)
    ax.title.set_size(TITLE_SIZE)
    sns.barplot(data=overall_results, x="dist", y=metric, hue="template", ax=ax, errorbar=None, palette="rocket")
    ax.legend(title="Instruction lang", title_fontsize=LEGEND_TITLE_SIZE, fontsize=LEGEND_SIZE)
    plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_s{num_shots}_{'_vs_'.join(templates)}.{output_format}"
    print(f"Saving figure to {plot_path}")
    plt.savefig(plot_path)

def plot_results_tok_aligned(tab_results_lst, output_dir, output_format="png", metric="accuracy", task="morph-gen", max_affix_length=10, num_shots=5):
    templates = [_get_template(tab_results) for tab_results in tab_results_lst]
    models = [_get_model(tab_results) for tab_results in tab_results_lst]
    languages = [_get_language(tab_results) for tab_results in tab_results_lst]

    assert len(set(languages)) == 1, "All tabulated results must be for the same language."
    assert len(set(templates)) == 1, "All tabulated results must be for the same template."
    assert len(set(models)) == 1, "All tabulated results must be for the same model."

    output_dir = pathlib.Path(output_dir) / f"{output_format}_figs_{languages[0]}_{templates[0]}_{models[0]}"
    output_dir.mkdir(parents=True, exist_ok=True)

    tab_results_lst[0]["tok_aligned"] = "Yes"
    tab_results_lst[1]["tok_aligned"] = "No"

    merged_results = pd.concat(tab_results_lst)

    results = merged_results.query(f"task == '{task}' & is_ood == False & num_affixes <= {max_affix_length} & num_shots == {num_shots}")
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.set_title(f"{TASK_TITLE_MAP[task]} - {metric.capitalize()}")
    ax.set_xlabel("Number of affixes", size=XLABEL_SIZE)
    ax.set_ylabel(metric.capitalize(), size=YLABEL_SIZE)
    ax.tick_params(axis='x', labelsize=TICK_SIZE)
    ax.tick_params(axis='y', labelsize=TICK_SIZE)
    ax.title.set_size(TITLE_SIZE)
    sns.barplot(data=results, x="num_affixes", y=metric, hue="tok_aligned", ax=ax, errorbar=None, palette="rocket")
    ax.legend(title="Tokenizer aligned", title_fontsize=LEGEND_TITLE_SIZE, fontsize=LEGEND_SIZE)
    plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_s{num_shots}_tok_vs_morph_aligned.{output_format}"
    print(f"Saving figure to {plot_path}")
    plt.savefig(plot_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--tab-results-paths", type=str, nargs="+", help="Path to tabulated results file(s)", required=True)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory to save plots", default=None)
    parser.add_argument("-e", "--metrics", type=str, choices=METRICS, default=METRICS, help="Metrics to show results for.")
    parser.add_argument("-f", "--output-format", type=str, choices=["png", "pdf", "svg"], default="png", help="Format to save the plots in.")
    parser.add_argument("-mal", "--max-affix-length", type=int, help="Maximum affix length to consider", default=7)
    parser.add_argument("-ns", "--num-shots", type=int, help="Number of shots to consider", default=5)
    parser.add_argument("-p", "--plot-types", type=str, nargs="+", choices=["main", "by_freq", "overall", "by_dist", "by_lang", "by_alignment"], default=["main", "overall", "by_dist"], help="Type of plots to generate")
    
    args = parser.parse_args()

    tab_results_lst = []

    for tab_results_path in args.tab_results_paths:
        results_path = pathlib.Path(tab_results_path)

        try:
            if results_path.suffix == ".csv":
                tab_results = pd.read_csv(results_path)
                tab_results_lst.append(tab_results)
            else:
                raise ValueError("Tabulated results extension not supported.")
        except FileNotFoundError:
            print(f"Skipping. Tabulated results file not found at {results_path}")
            return

    output_dir = args.output_dir

    if output_dir is None:
        output_dir = results_path.parent / "figures"
    
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

    for metric in args.metrics:
        for task in ["morph-disc", "morph-gen"]:
            if len(tab_results_lst) > 1:
                if "by_lang" in args.plot_types:
                    plot_results_by_lang(tab_results_lst,
                                        output_dir=output_dir,
                                        output_format=args.output_format,
                                        metric=metric,
                                        task=task,
                                        max_affix_length=args.max_affix_length,
                                        num_shots=args.num_shots)
                elif "by_alignment" in args.plot_types:
                    plot_results_tok_aligned(tab_results_lst,
                                        output_dir=output_dir,
                                        output_format=args.output_format,
                                        metric=metric,
                                        task=task,
                                        max_affix_length=args.max_affix_length,
                                        num_shots=args.num_shots)
                else:
                    raise ValueError("Invalid plot type for multiple tabulated results.")
            else:
                if "by_dist" in args.plot_types:
                    plot_results_id_vs_ood(tab_results_lst,
                                        output_dir=output_dir,
                                        output_format=args.output_format,
                                        metric=metric,
                                        task=task,
                                        max_affix_length=args.max_affix_length,
                                        num_shots=args.num_shots)
                if "overall" in args.plot_types:
                    plot_results_overall(tab_results_lst,
                                        output_dir=output_dir,
                                        output_format=args.output_format,
                                        metric=metric,
                                        task=task,
                                        max_affix_length=args.max_affix_length)
                for is_ood in [False, True]:
                    if "by_freq" in args.plot_types and "freq_bin" in tab_results.columns:
                        keyword = "unigram" 
                        if "meta_suffix" in results_path.name:
                            keyword = "meta suffix"
                        elif "suffix" in results_path.name:
                            keyword = "suffix"

                        plot_results_by_freq(tab_results_lst, 
                                            output_dir=output_dir, 
                                            output_format=args.output_format, 
                                            metric=metric,
                                            task=task,
                                            is_ood=is_ood,
                                            keyword=keyword,
                                            max_affix_length=args.max_affix_length)
                    elif "main" in args.plot_types:
                        plot_results(tab_results_lst, 
                                output_dir=output_dir, 
                                output_format=args.output_format,
                                metric=metric,
                                task=task,
                                is_ood=is_ood,
                                max_affix_length=args.max_affix_length)

if __name__ == "__main__":
    main()