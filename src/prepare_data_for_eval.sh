#!/bin/bash

version=_sent
shots=(1 3 5)
suffix=""
data_dir="../experiments/data"

for shot in "${shots[@]}"
do
    # TR in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample${suffix}.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample${suffix}.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce${suffix}.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce${suffix}.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/v${version} -m

    # # TR in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample${suffix}.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample${suffix}.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce${suffix}.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce${suffix}.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/v${version} -m

    # TR in EN template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph${suffix}.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph${suffix}.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce${suffix}.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce${suffix}.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/v${version} -m

    # # TR in TR template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph${suffix}.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph${suffix}.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce${suffix}.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/v${version} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce${suffix}.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/v${version} -m

    # EN in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph${suffix}.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph${suffix}.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce${suffix}.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce${suffix}.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/v${version} -m
    
    # EN in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph${suffix}.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph${suffix}.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce${suffix}.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/v${version} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce${suffix}.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/v${version} -m
done