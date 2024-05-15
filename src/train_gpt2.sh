#!/bin/bash

modelname=gpt2

MNT_POINT=/mnt/u14157_ic_nlp_001_files_nfs


if ! [ -d ${MNT_POINT} ]; then
    MNT_POINT=/mnt
fi

export WANDB_API_KEY=$(cat ${MNT_POINT}/nlpdata1/home/ismayilz/.wandb.key)
export WANDB_PROJECT=project-morphgen

python run_clm.py \
    --model_name_or_path ${modelname} \
    --dataset_name wikimedia/wikipedia \
    --dataset_config_name 20231101.tr \
    --num_train_epochs 1 \
    --block_size 256 \
    --per_device_train_batch_size 64 \
    --per_device_eval_batch_size 64 \
    --prediction_loss_only \
    --dataloader_num_workers 32 \
    --preprocessing_num_workers 32 \
    --gradient_accumulation_steps 2 \
    --learning_rate 0.00005 \
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
    --output_dir "${MNT_POINT}/nlpdata1/home/ismayilz/project-morphgen/morph-gen-wiki/models/${modelname}" \
    --cache_dir "${MNT_POINT}/nlpdata1/home/ismayilz/.cache" \
    --report_to wandb