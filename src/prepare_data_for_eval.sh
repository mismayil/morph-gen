#!/bin/bash

version=2
shots=(1 3)

for shot in "${shots[@]}"
do
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_gen_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_disc_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_gen_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_disc_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
done

for shot in "${shots[@]}"
do
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_gen_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_disc_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_disc_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
done