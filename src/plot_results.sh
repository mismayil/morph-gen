#!/bin/bash

model=${1:-"gpt-3.5-turbo"}
version=${2:-"_aligned_tok"}

python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version}/tab_results.csv -o ../figures/v${version} -l tr -t en -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version}/tab_results.csv -o ../figures/v${version} -l tr -t tr -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}/tab_results.csv -o ../figures/v${version} -l en -t en -m ${model}
python plot_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}/tab_results.csv -o ../figures/v${version} -l en -t tr -m ${model}