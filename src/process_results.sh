#!/bin/bash

experiment_dir=${1:-"../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1"}
experiment_name=${2:-"v_final_default"}
figures_dir="../experiments/figures"

python report_metrics.py -r ${experiment_dir}
python tabulate_results.py -r ${experiment_dir}

# plot TR results
python plot_results.py -r ${experiment_dir}/tab_results.csv -o ${figures_dir}/tr/final/${experiment_name}/batch1

# plot FI results
# python plot_results.py -r ${experiment_dir}/tab_results.csv -o ${figures_dir}/fi/final/${experiment_name}