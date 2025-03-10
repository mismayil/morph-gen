#!/bin/bash

experiment=${1:-"v_final_default"}
model_version=${2:-"8"}  # 8, 35
model="aya-23-${model_version}b"
model_path="CohereForAI/aya-23-${model_version}b"
tokenizer_path="CohereForAI/aya-23-${model_version}b"
cache_dir=${4:-"/mnt/scratch/home/ismayilz/.cache/huggingface/hub"}
input_dir=${5:-${experiment}}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# TR default experiments (temp_en)
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

# TR default experiments (temp_tr)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} \
#                           -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 \
#                           -m ${model} \
#                           -b 4 \
#                           -mp ${model_path} \
#                           -tp ${tokenizer_path} \
#                           -c ${cache_dir}
# done