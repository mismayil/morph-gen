#!/bin/bash

openai_api_key=$1
model=${2:-"gpt-3.5-turbo"}
version=4

# for jsonfile in ../data/tr/btwd/temp_en/v${version}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ../outputs/${model}/tr/btwd/temp_en/v${version} -k ${openai_api_key} -m ${model}
# done

# for jsonfile in ../data/tr/btwd/temp_tr/v${version}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ../outputs/${model}/tr/btwd/temp_tr/v${version} -k ${openai_api_key} -m ${model}
# done

# for jsonfile in ../data/en/morpholex/temp_en/v${version}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ../outputs/${model}/en/morpholex/temp_en/v${version} -k ${openai_api_key} -m ${model}
# done

# for jsonfile in ../data/en/morpholex/temp_tr/v${version}/*.json
# do
#     echo "Evaluating ${jsonfile}"
#     python evaluate_gpt.py -d ${jsonfile} -o ../outputs/${model}/en/morpholex/temp_tr/v${version} -k ${openai_api_key} -m ${model}
# done

shots=(1 3 5)
for shot in "${shots[@]}"
do
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_eval_morph_gen_en_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_en/v${version} -k ${openai_api_key} -m ${model}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_eval_morph_disc_en_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_en/v${version} -k ${openai_api_key -m ${model}}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_gen_en_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_en/v${version} -k ${openai_api_key} -m ${model}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_en/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_disc_en_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_en/v${version} -k ${openai_api_key} -m ${model}

    # python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_eval_morph_gen_tr_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_tr/v${version} -k ${openai_api_key} -m ${model}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_eval_morph_disc_tr_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_tr/v${version} -k ${openai_api_key} -m ${model}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_gen_tr_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_tr/v${version} -k ${openai_api_key} -m ${model}
    # python evaluate_gpt.py -d ../data/tr/btwd/temp_tr/v${version}/btwd_prep_post_sample_morph_nonce_eval_morph_disc_tr_s${shot}.json -o ../outputs/${model}/tr/btwd/temp_tr/v${version} -k ${openai_api_key} -m ${model}

    python evaluate_gpt.py -d ../data/en/morpholex/temp_en/v${version}/MorphoLEX_en_prep_morph_sample_nonce_sep+_eval_morph_gen_en_s${shot}.json -o ../outputs/${model}/en/morpholex/temp_en/v${version} -k ${openai_api_key} -m ${model}
    python evaluate_gpt.py -d ../data/en/morpholex/temp_en/v${version}/MorphoLEX_en_prep_morph_sample_nonce_sep+_eval_morph_disc_en_s${shot}.json -o ../outputs/${model}/en/morpholex/temp_en/v${version} -k ${openai_api_key} -m ${model}

    python evaluate_gpt.py -d ../data/en/morpholex/temp_tr/v${version}/MorphoLEX_en_prep_morph_sample_nonce_sep+_eval_morph_gen_tr_s${shot}.json -o ../outputs/${model}/en/morpholex/temp_tr/v${version} -k ${openai_api_key} -m ${model}
    python evaluate_gpt.py -d ../data/en/morpholex/temp_tr/v${version}/MorphoLEX_en_prep_morph_sample_nonce_sep+_eval_morph_disc_tr_s${shot}.json -o ../outputs/${model}/en/morpholex/temp_tr/v${version} -k ${openai_api_key} -m ${model}
done