#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"random"}
input_dir=${3:-${experiment}}
api_key=${4}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# tr default experiments
for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_baseline.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model}
done

# # fi default experiments
for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_baseline.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} -m ${model}
done