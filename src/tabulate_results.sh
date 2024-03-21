#!/bin/bash

model=${1:-"gpt-4"}
version=${2:-"_balanced"}

# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}
# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version}