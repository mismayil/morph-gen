#!/bin/bash

openai_api_key=$1
model=${2:-"gpt-3.5-turbo"}
experiment=${3:-"v_sent"}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# for jsonfile in ${data_dir}/tr/btwd/eval/temp_en/${experiment}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

# for jsonfile in ${data_dir}/tr/btwd/eval/temp_tr/${experiment}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

for jsonfile in ${data_dir}/tr/sense/eval/temp_en/${experiment}/*.json
do
    if [[ $jsonfile == *"nonce"* ]]; then
        echo "Evaluating ${jsonfile}"
        python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
    fi
done

for jsonfile in ${data_dir}/tr/sense/eval/temp_tr/${experiment}/*.json
do
    if [[ $jsonfile == *"nonce"* ]]; then
        echo "Evaluating ${jsonfile}"
        python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
    fi
done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_en/${experiment}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_tr/${experiment}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
# done