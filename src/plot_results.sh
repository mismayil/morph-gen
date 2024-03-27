#!/bin/bash

model=${1:-"gpt-4"}
experiment=${2:-"v_balanced"}

# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t tr -m ${model}

python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}/tab_results_by_freq.csv -o ../experiments/figures/${experiment} -l en -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}/tab_results_by_freq.csv -o ../experiments/figures/${experiment} -l en -t tr -m ${model}