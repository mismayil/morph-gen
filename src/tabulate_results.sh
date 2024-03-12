#!/bin/bash

model=${1:-"gpt-3.5-turbo"}
version=${2:-"_aligned_tok"}

python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}
python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version}