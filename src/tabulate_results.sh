#!/bin/bash

model=${1:-"gpt-4"}
experiment=${2:-"v_balanced"}

# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}
# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment}
python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment}

# python tabulate_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}
# python tabulate_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}