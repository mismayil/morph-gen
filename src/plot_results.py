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
    "coherence": "coh",
}


def plot_results(
    tab_results,
    output_dir,
    output_format="png",
    language="en",
    template="en",
    model="gpt-3.5-turbo",
    metric="accuracy",
    task="morph-gen",
    is_ood=False,
    max_suffix_length=10,
):
    results = tab_results.query(
        f"is_ood == {is_ood} & task == '{task}' & num_suffixes <= {max_suffix_length}"
    )
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.set_title(
            f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, dist={'OOD' if is_ood else 'ID'}, task={task}]"
        )
        ax.set_xlabel("Number of suffixes")
        ax.set_ylabel(metric.capitalize())
        ax.title.set_size(20)
        sns.barplot(
            data=results,
            x="num_suffixes",
            y=metric,
            hue="num_shots",
            ax=ax,
            errorbar=None,
        )
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_{'ood' if is_ood else 'id'}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)


def plot_results_by_freq(
    tab_results,
    output_dir,
    output_format="png",
    language="en",
    template="en",
    model="gpt-3.5-turbo",
    metric="accuracy",
    task="morph-gen",
    is_ood=False,
    keyword="unigram",
    max_suffix_length=10,
):
    results = tab_results.query(
        f"is_ood == {is_ood} & task == '{task}' & num_suffixes <= {max_suffix_length}"
    )
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, axes = plt.subplots(figsize=(16, 8), nrows=1, ncols=2)

        axes[0].set_title(
            f"{metric.capitalize()} by frequency \n [lang={language}, temp={template}, model={model}] \n [dist={'OOD' if is_ood else 'ID'}, task={task}]"
        )
        axes[0].set_xlabel(f"{keyword.capitalize()} frequency")
        axes[0].set_ylabel(metric.capitalize())
        axes[0].title.set_size(20)
        sns.barplot(data=results, x="freq_bin", y=metric, hue="num_shots", ax=axes[0])

        axes[1].set_title(
            f"Number of samples by suffix length and frequency \n [lang={language}, temp={template}, model={model}] \n [dist={'OOD' if is_ood else 'ID'}, task={task}]"
        )
        axes[1].set_xlabel(f"{keyword.capitalize()} frequency")
        axes[1].set_ylabel("Number of samples")
        axes[1].title.set_size(20)
        sns.barplot(
            data=results, x="freq_bin", y="num_samples", hue="num_suffixes", ax=axes[1]
        )

        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_by_{keyword.replace(' ', '_')}_freq_{task}_{'ood' if is_ood else 'id'}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)


def plot_results_id_vs_ood(
    tab_results,
    output_dir,
    output_format="png",
    language="en",
    template="en",
    model="gpt-3.5-turbo",
    metric="accuracy",
    task="morph-gen",
    max_suffix_length=10,
    num_shots=5,
):
    results = tab_results.query(
        f"task == '{task}' & num_suffixes <= {max_suffix_length} & num_shots == {num_shots}"
    ).copy()
    if len(results) > 0 and any(results[metric] > 0):
        plt.ioff()
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.set_title(
            f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, num_shots={num_shots}, task={task}]"
        )
        ax.set_xlabel("Number of suffixes")
        ax.set_ylabel(metric.capitalize())
        ax.title.set_size(20)
        results["dist"] = results["is_ood"].replace({False: "ID", True: "OOD"})
        sns.barplot(
            data=results,
            x="num_suffixes",
            y=metric,
            hue="dist",
            hue_order=["ID", "OOD"],
            ax=ax,
            errorbar=None,
            palette="rocket",
        )
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_s{num_shots}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)


def plot_results_overall(
    tab_results,
    output_dir,
    output_format="png",
    language="en",
    template="en",
    model="gpt-3.5-turbo",
    metric="accuracy",
    task="morph-gen",
    max_suffix_length=10,
):
    results = tab_results.query(
        f"task == '{task}' & num_suffixes <= {max_suffix_length}"
    ).copy()
    if len(results) > 0 and any(results[metric] > 0):
        overall_results = (
            results.groupby(["task", "is_ood", "num_shots"])
            .agg(
                {
                    "accuracy": "mean",
                    "f1": "mean",
                    "coherence": "mean",
                    "faithfulness": "mean",
                }
            )
            .reset_index()
        )
        plt.ioff()
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.set_title(
            f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, task={task}]"
        )
        ax.set_xlabel("Test Distribution")
        ax.set_ylabel(metric.capitalize())
        ax.title.set_size(20)
        overall_results["dist"] = overall_results["is_ood"].replace(
            {False: "ID", True: "OOD"}
        )
        sns.barplot(
            data=overall_results,
            x="dist",
            y=metric,
            hue="num_shots",
            ax=ax,
            errorbar=None,
        )
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--tab-results-path",
        type=str,
        help="Path to tabulated results file",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        help="Output directory to save plots",
        default="../figures",
    )
    parser.add_argument(
        "-l", "--language", type=str, help="Experiment language", required=True
    )
    parser.add_argument(
        "-t", "--template", type=str, help="Experiment template", required=True
    )
    parser.add_argument(
        "-m", "--model", type=str, help="Experiment model", required=True
    )
    parser.add_argument(
        "-e",
        "--metrics",
        type=str,
        choices=METRICS,
        default=METRICS,
        help="Metrics to show results for.",
    )
    parser.add_argument(
        "-f",
        "--output-format",
        type=str,
        choices=["png", "pdf"],
        default="png",
        help="Format to save the plots in.",
    )
    parser.add_argument(
        "-msl",
        "--max-suffix-length",
        type=int,
        help="Maximum suffix length to consider",
        default=7,
    )
    parser.add_argument(
        "-ns", "--num-shots", type=int, help="Number of shots to consider", default=5
    )

    args = parser.parse_args()

    results_path = pathlib.Path(args.tab_results_path)

    try:
        if results_path.suffix == ".csv":
            tab_results = pd.read_csv(results_path)
        else:
            raise ValueError("Tabulated results extension not supported.")
    except FileNotFoundError:
        print(f"Skipping. Tabulated results file not found at {results_path}")
        return

    output_dir = (
        pathlib.Path(args.output_dir)
        / f"figs_{args.language}_{args.template}_{args.model}"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    for metric in args.metrics:
        for task in ["morph-disc", "morph-gen"]:
            plot_results_id_vs_ood(
                tab_results,
                output_dir=output_dir,
                output_format=args.output_format,
                language=args.language,
                template=args.template,
                model=args.model,
                metric=metric,
                task=task,
                max_suffix_length=args.max_suffix_length,
                num_shots=args.num_shots,
            )
            plot_results_overall(
                tab_results,
                output_dir=output_dir,
                output_format=args.output_format,
                language=args.language,
                template=args.template,
                model=args.model,
                metric=metric,
                task=task,
                max_suffix_length=args.max_suffix_length,
            )
            for is_ood in [False, True]:
                if "freq_bin" in tab_results.columns:
                    keyword = "unigram"
                    if "meta_suffix" in results_path.name:
                        keyword = "meta suffix"
                    elif "suffix" in results_path.name:
                        keyword = "suffix"

                    plot_results_by_freq(
                        tab_results,
                        output_dir=output_dir,
                        output_format=args.output_format,
                        language=args.language,
                        template=args.template,
                        model=args.model,
                        metric=metric,
                        task=task,
                        is_ood=is_ood,
                        keyword=keyword,
                        max_suffix_length=args.max_suffix_length,
                    )
                else:
                    plot_results(
                        tab_results,
                        output_dir=output_dir,
                        output_format=args.output_format,
                        language=args.language,
                        template=args.template,
                        model=args.model,
                        metric=metric,
                        task=task,
                        is_ood=is_ood,
                        max_suffix_length=args.max_suffix_length,
                    )


if __name__ == "__main__":
    main()
