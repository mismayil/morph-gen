#!/bin/bash

experiment=${1:-"v_sent"}
model=${2:-"gpt-3.5-turbo"}
openai_api_key=${3}
input_dir=${4:-${experiment}}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# mkdir -p ./logs

# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/*.json
# do
    # echo "Evaluating ${jsonfile}"
    # python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia > ./logs/$(basename ${jsonfile}).log 2>&1 &
    # python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/gpt-2/tr/btwd/temp_en/${experiment} -m ${model} -mp mismayil/tr_gpt2 -tp gpt2 -c /mnt/u14157_ic_nlp_001_files_nfs/nlpdata1/home/ismayilz/.cache/huggingface
    # python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/gpt-2-ttok/tr/btwd/temp_en/${experiment} -m gpt-2 -mp /home/azureuser/morph-gen-artifacts/tr_gpt2_pretrained6 -tp /home/azureuser/morph-gen-artifacts/tr_gpt2_pretrained6
# done

for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    # python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia > ./logs/$(basename ${jsonfile}).log 2>&1 &
    python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/${experiment} -k ${openai_api_key} -m ${model}
done

for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/*.json
do
    echo "Evaluating ${jsonfile}"
    python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia > ./logs/$(basename ${jsonfile}).log 2>&1 &
done

# for jsonfile in ${data_dir}/tr/sense/eval/temp_en/${input_dir}/*.json
# do
#     if [[ $jsonfile == *"nonce"* ]]; then
#         echo "Evaluating ${jsonfile}"
#         python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
#     fi
# done

# for jsonfile in ${data_dir}/tr/sense/eval/temp_tr/${input_dir}/*.json
# do
#     if [[ $jsonfile == *"nonce"* ]]; then
#         echo "Evaluating ${jsonfile}"
#         python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/sense/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
#     fi
# done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_en/${experiment} -k ${openai_api_key} -m ${model} -ia
# done

# for jsonfile in ${data_dir}/en/morpholex/eval/temp_tr/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ${outputs_dir}/${model}/en/morpholex/temp_tr/${experiment} -k ${openai_api_key} -m ${model} -ia
# done
