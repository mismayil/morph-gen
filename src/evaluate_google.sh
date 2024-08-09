#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"gemini-1.5-flash"}
input_dir=${3:-${experiment}}
api_key=${4}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 4
done

# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 4
# done

# for jsonfile in ${data_dir}/tr/btwd/test/eval/temp_tr/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/test/${experiment} -m ${model} -ia -b 4 -t 0.3
# done
# cot experiments
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment} -m ${model} -ia -b 1 --max-tokens None
# done

# for jsonfile in ${data_dir}/tr/sense/eval/temp_en/${input_dir}/*.json
# do
#     if [[ $jsonfile == *"nonce"* ]]; then
#         echo "Evaluating ${jsonfile}"
#         python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
#     fi
# done

# for jsonfile in ${data_dir}/tr/sense/eval/temp_tr/${input_dir}/*.json
# do
#     if [[ $jsonfile == *"nonce"* ]]; then
#         echo "Evaluating ${jsonfile}"
#         python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
#     fi
# done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_tr/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

# for jsonfile in ${data_dir}/fi/test/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/test/temp_en/${experiment} -m ${model} -ia -b 4
# done
