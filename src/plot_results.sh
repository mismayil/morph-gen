#!/bin/bash

model=${1:-"gpt-4"}
experiment=${2:-"v_balanced"}

# Default TR experiments
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/final/${experiment}/tab_results.csv -o ../experiments/figures/final/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/final/${experiment}/tab_results.csv -o ../experiments/figures/final/${experiment} -l tr -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}/tab_results_by_freq.csv -o ../experiments/figures/${experiment} -l en -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}/tab_results_by_freq.csv -o ../experiments/figures/${experiment} -l en -t tr -m ${model}


# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}
# # python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t en -m ${model}
# # python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}/tab_results.csv -o ../experiments/figures/${experiment} -l en -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}/tab_results_by_unigram_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}/tab_results_by_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t en -m ${model}
# python plot_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}/tab_results_by_meta_suffix_freq.csv -o ../experiments/figures/${experiment} -l tr -t tr -m ${model}

# Paper figures
python plot_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/test/v3_balanced_no_quote/tab_results.csv -o ../experiments/figures/test/v3_balanced_no_quote -f svg
python plot_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/test/v_sent_no_quote/tab_results.csv -o ../experiments/figures/test/v_sent_no_quote -f svg
python plot_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_tr/test/v3_balanced_no_quote/tab_results.csv -o ../experiments/figures/test/v3_balanced_no_quote -f svg
python plot_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/test/v3_balanced_no_quote/tab_results.csv ../experiments/outputs/gpt-4/tr/btwd/temp_tr/test/v3_balanced_no_quote/tab_results.csv -o ../experiments/figures/test/v3_balanced_no_quote -f svg