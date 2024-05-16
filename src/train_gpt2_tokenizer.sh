#!/bin/bash

MNT_POINT=/mnt/u14157_ic_nlp_001_files_nfs

if ! [ -d ${MNT_POINT} ]; then
    MNT_POINT=/mnt
fi

model=gpt2

python train_tokenizer.py \
    -m ${model} \
    -o ${MNT_POINT}/nlpdata1/home/ismayilz/project-morphgen/morph-gen-wiki/tokenizers/${model} \
    -d mismayil/tr_wikipedia \
    -c ${MNT_POINT}/nlpdata1/home/ismayilz/.cache
