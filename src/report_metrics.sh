#!/bin/bash

model=${1:-"gpt-4"}
experiment=${2:-"v_balanced"}

# python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_en/${experiment}
# python report_metrics.py -r ../experiments/outputs/${model}/en/morpholex/temp_tr/${experiment}
# python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_en/${experiment} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json
# python report_metrics.py -r ../experiments/outputs/${model}/tr/btwd/temp_tr/${experiment} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json

python report_metrics.py -r ../experiments/outputs/${model}/tr/sense/temp_en/${experiment} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json
python report_metrics.py -r ../experiments/outputs/${model}/tr/sense/temp_tr/${experiment} -uf ../data/tr/bilkent-turkish-writings/btwd_unigram_freq.json -sf ../data/tr/bilkent-turkish-writings/btwd_morpheme_freq.json -mf ../data/tr/bilkent-turkish-writings/btwd_meta_morpheme_freq.json