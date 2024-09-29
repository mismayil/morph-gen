#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"gemini-1.5-flash"}
input_dir=${3:-${experiment}}
api_key=${4}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# tr default experiments (temp_en)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 8
# done

# # tr default experiments (temp_tr)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 8
# done

# # tr cot experiments (temp_en)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 4 -g None
# done

# # tr cot experiments (temp_tr)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 4 -g None
# done

# fi default experiments (temp_en)
for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} -m ${model} -b 8
done

# # fi default experiments (temp_fi)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_fi/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_fi/v4/${experiment} -m ${model} -b 8
# done

# fi cot experiments (temp_en)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} -m ${model} -b 4 -g None
# done

# fi cot experiments (temp_fi)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_fi/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_fi/v4/${experiment} -m ${model} -b 4 -g None
# done