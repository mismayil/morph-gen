import argparse
import pathlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

METRICS = ["faithfulness", "accuracy"]

ABBR_METRICS = {
    "faithfulness": "faith",
    "accuracy": "acc"
}

def plot_results(tab_results, output_dir, output_format="png", language="en", template="en", model="gpt-3.5-turbo",  metric="accuracy", task="morph-gen", is_ood=False):
    results = tab_results.query(f"is_ood == {is_ood} & task == '{task}'")
    if len(results) > 0:
        plt.ioff()
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.set_title(f"{metric.capitalize()} \n [lang={language}, temp={template}, model={model}, dist={'OOD' if is_ood else 'ID'}, task={task}]")
        ax.set_xlabel("Number of suffixes")
        ax.set_ylabel(metric.capitalize())
        ax.title.set_size(20)
        sns.barplot(data=results, x="num_suffixes", y=metric, hue="num_shots", ax=ax, errorbar=None)
        plot_path = f"{output_dir}/fig_{ABBR_METRICS[metric]}_{task}_{'ood' if is_ood else 'id'}.{output_format}"
        print(f"Saving figure to {plot_path}")
        plt.savefig(plot_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--tab-results-path", type=str, help="Path to tabulated results file", required=True)
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory to save plots", default="../figures")
    parser.add_argument("-l", "--language", type=str, help="Experiment language", required=True)
    parser.add_argument("-t", "--template", type=str, help="Experiment template", required=True)
    parser.add_argument("-m", "--model", type=str, help="Experiment model", required=True)
    parser.add_argument("-e", "--metrics", type=str, choices=METRICS, default=METRICS, help="Metrics to show results for.")
    parser.add_argument("-f", "--output-format", type=str, choices=["png", "pdf"], default="png", help="Format to save the plots in.")

    args = parser.parse_args()

    results_path = pathlib.Path(args.tab_results_path)

    if results_path.suffix == ".csv":
        tab_results = pd.read_csv(results_path)
    else:
        raise ValueError("Tabulated results extension not supported.")

    output_dir = pathlib.Path(args.output_dir) / f"figs_{args.language}_{args.template}_{args.model}"
    output_dir.mkdir(parents=True, exist_ok=True)

    for metric in args.metrics:
        for task in ["morph-disc", "morph-gen"]:
            for is_ood in [False, True]:
                plot_results(tab_results, 
                             output_dir=output_dir, 
                             output_format=args.output_format, 
                             language=args.language, 
                             template=args.template,
                             model=args.model,
                             metric=metric,
                             task=task,
                             is_ood=is_ood)

if __name__ == "__main__":
    main()