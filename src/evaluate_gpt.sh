#!/bin/bash

openai_api_key=$1
version=2
shots=(1 3)

# for shot in "${shots[@]}"
# do
#     python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_eval_morph_gen_en_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_en/v${version} -k ${openai_api_key}
#     python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_eval_morph_disc_en_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_en/v${version} -k ${openai_api_key}
#     python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_gen_en_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_en/v${version} -k ${openai_api_key}
#     python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_disc_en_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_en/v${version} -k ${openai_api_key}
# done

for shot in "${shots[@]}"
do
    python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_eval_morph_gen_tr_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_tr/v${version} -k ${openai_api_key}
    python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_eval_morph_disc_tr_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_tr/v${version} -k ${openai_api_key}
    python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_gen_tr_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_tr/v${version} -k ${openai_api_key}
    python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_disc_tr_s${shot}.json -o ../outputs/gpt-3.5/tr/btwd/temp_tr/v${version} -k ${openai_api_key}
done