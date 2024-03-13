#!/bin/bash

model=${1:-"gpt-3.5-turbo"}
version=${2:-"_aligned_tok"}

python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}
python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}
python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version} -f ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json
python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version} -f ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json