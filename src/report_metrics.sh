#!/bin/bash

model=${1:-"gpt-3.5-turbo"}
version=_balanced

python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}
python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}
# python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version}
# python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version}