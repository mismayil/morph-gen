#!/bin/bash

MNT_POINT=/mnt/u14157_ic_nlp_001_files_nfs

if ! [ -d ${MNT_POINT} ]; then
    MNT_POINT=/mnt
fi

# export WANDB_API_KEY=$(cat ${MNT_POINT}/nlpdata1/home/ismayilz/.wandb.key)
export WANDB_PROJECT=project-morphgen

model_path=gpt2
tokenizer_path=${HOME}/morph-gen-artifacts/tr_gpt2_tokenizer_v1k
# tokenizer_path=mismayil/tr_gpt2_tokenizer
# tokenizer_path=gpt2
# model_path=${HOME}/tr_gpt2_pretrained
# output_dir="${MNT_POINT}/nlpdata1/home/ismayilz/project-morphgen/morph-gen-wiki/models/${modelname}"
output_dir=${HOME}/morph-gen-artifacts/tr_gpt2_pretrained_v1k
# cache_dir="${MNT_POINT}/nlpdata1/home/ismayilz/.cache"
cache_dir=${HOME}/.cache/huggingface/hub

python run_clm.py \
    --model_name_or_path ${model_path} \
    --dataset_name mismayil/tr_wikipedia \
    --tokenizer_name ${tokenizer_path} \
    --num_train_epochs 1 \
    --block_size 256 \
    --per_device_train_batch_size 64 \
    --per_device_eval_batch_size 64 \
    --prediction_loss_only \
    --dataloader_num_workers 32 \
    --preprocessing_num_workers 32 \
    --gradient_accumulation_steps 2 \
    --learning_rate 0.0005 \
    --warmup_steps 500 \
    --save_total_limit 2 \
    --save_steps 1000 \
    --save_strategy steps \
    --eval_steps 1000 \
    --evaluation_strategy steps \
    --logging_steps 100 \
    --logging_first_step \
    --do_train \
    --do_eval \
    --output_dir ${output_dir} \
    --cache_dir ${cache_dir} \
    --report_to wandb \
    --seed 42 \
    --run_name gpt2-tr-wiki-e1-c256-b64-lr5e-4-ttok-v1k