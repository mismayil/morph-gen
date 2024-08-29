#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"aya-23-35b"}
model_path=${3:-"CohereForAI/aya-23-35b"}
tokenizer_path=${3:-"CohereForAI/aya-23-35b"}
cache_dir=${4:-"/mnt/nlpdata1/home/ismayilz/.cache/huggingface/hub"}
input_dir=${5:-${experiment}}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} \
                          -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 \
                          -m ${model} \
                          -b 4 \
                          -mp ${model_path} \
                          -tp ${tokenizer_path} \
                          -c ${cache_dir}
done
