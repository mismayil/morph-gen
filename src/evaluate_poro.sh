#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"poro-34b"}
model_path=${3:-"LumiOpen/Poro-34B-chat"}
tokenizer_path=${3:-"LumiOpen/Poro-34B-chat"}
cache_dir=${4:-"/mnt/scratch/home/ismayilz/.cache/huggingface/hub"}
input_dir=${5:-${experiment}}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# FI default experiments (temp_en)
for jsonfile in ${data_dir}/fi/v3/eval/temp_en/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} \
                          -o ${outputs_dir}/${model}/fi/temp_en/v3/${experiment} \
                          -m ${model} \
                          -b 4 \
                          -mp ${model_path} \
                          -tp ${tokenizer_path} \
                          -c ${cache_dir}
done

# # FI default experiments (temp_fi)
# for jsonfile in ${data_dir}/fi/v3/eval/temp_fi/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} \
#                           -o ${outputs_dir}/${model}/fi/temp_fi/v3/${experiment} \
#                           -m ${model} \
#                           -b 4 \
#                           -mp ${model_path} \
#                           -tp ${tokenizer_path} \
#                           -c ${cache_dir}
# done