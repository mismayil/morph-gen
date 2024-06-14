#!/bin/bash

model=${1:-"gpt-4"}
experiment=${2:-"v_balanced"}

# Default TR experiments
# python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/final/${experiment}
# python tabulate_results.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/final/${experiment}

# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}
# python tabulate_results.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}

# python tabulate_results.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment}
# python tabulate_results.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment}

python tabulate_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/test/v3_balanced_no_quote
python tabulate_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/test/v_sent_no_quote
python tabulate_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_tr/test/v3_balanced_no_quote