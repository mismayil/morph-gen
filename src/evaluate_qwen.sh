#!/bin/bash

experiment=${1:-"v_final_default"}
model_version=${2:-"7"} # 7, 14, 32
model="qwen-2.5-${model_version}b"
model_path="Qwen/Qwen2.5-${model_version}B-Instruct"
tokenizer_path="Qwen/Qwen2.5-${model_version}B-Instruct"
cache_dir=${4:-"/mnt/scratch/home/ismayilz/.cache/huggingface/hub"}
input_dir=${5:-${experiment}}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# FI default experiments (temp_en)
for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} \
                          -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} \
                          -m ${model} \
                          -b 4 \
                          -mp ${model_path} \
                          -tp ${tokenizer_path} \
                          -c ${cache_dir}
done

# # FI default experiments (temp_fi)
for jsonfile in ${data_dir}/fi/v4/eval/temp_fi/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} \
                          -o ${outputs_dir}/${model}/fi/temp_fi/v4/${experiment} \
                          -m ${model} \
                          -b 4 \
                          -mp ${model_path} \
                          -tp ${tokenizer_path} \
                          -c ${cache_dir}
done