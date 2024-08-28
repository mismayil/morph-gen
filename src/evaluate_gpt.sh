#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"gpt-4"}
input_dir=${3:-${experiment}}
api_key=${4}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# tr default experiments
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 4 -oa
# done

# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 4
# done

# tr cot experiments
for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 2 -oa -g None
done

# fi default experiments
# for jsonfile in ${data_dir}/fi/final/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/final/${experiment} -m ${model} -b 8 -oa
# done