#!/bin/bash

experiment=${1:-"v_final_default"}
model=${2:-"gpt-4"}
input_dir=${3:-${experiment}}
api_key=${4}
data_dir="../experiments/data"
outputs_dir="../experiments/outputs"

# tr default experiments (temp_en)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 4 -oa
# done

# tr default experiments (temp_tr)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 4
# done

# # tr cot experiments (temp_en)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}/batch1 -m ${model} -b 2 -oa -g None
# done

# tr cot experiments (temp_tr)
# for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_tr/${input_dir}/batch1/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_tr/final/${experiment}/batch1 -m ${model} -b 4 -oa -g None
# done

# fi default experiments (temp_en)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} -m ${model} -b 8
# done

# # fi default experiments (temp_fi)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_fi/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_fi/v4/${experiment} -m ${model} -b 8 -oa
# done

# # fi cot experiments (temp_en)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_en/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_en/v4/${experiment} -m ${model} -b 4 -oa -g None
# done

# # fi cot experiments (temp_fi)
# for jsonfile in ${data_dir}/fi/v4/eval/temp_fi/${input_dir}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/fi/temp_fi/v4/${experiment} -m ${model} -b 4 -oa -g None
# done

# tr default experiments (temp_en) with temperature sampling
temperatures=(0.3 0.5 0.7 0.9)
for temperature in ${temperatures[@]}
do
    for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/s5/*.json
    do
        echo "Evaluating ${jsonfile}"
        python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}_t${temperature}/s5 -m ${model} -b 4 -t ${temperature} -p 1
    done
done

# tr default experiments (temp_en) with top_p sampling
top_ps=(0.9 0.95)
for top_p in ${top_ps[@]}
do
    for jsonfile in ${data_dir}/tr/btwd/final/eval/temp_en/${input_dir}/s5/*.json
    do
        echo "Evaluating ${jsonfile}"
        python evaluate_lm.py -d ${jsonfile} -o ${outputs_dir}/${model}/tr/btwd/temp_en/final/${experiment}_p${top_p}/s5 -m ${model} -b 4 -p ${top_p} -t 1
    done
done