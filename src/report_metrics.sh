#!/bin/bash

model=${1:-"gpt-4"}
version=${2:-"_balanced"}

# python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/v${version}
# python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/v${version}
python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/v${version} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json
python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/v${version} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json