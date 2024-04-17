#!/bin/bash

experiment=v_tok_aligned_sent
shots=(1 3 5)
data_dir="../experiments/data"

for shot in "${shots[@]}"
do
    # TR in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/temp_en/${experiment} -m

    # # TR in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/btwd_prep_post_balanced_morph_sample_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/temp_tr/${experiment} -m

    # TR in EN template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_morph_sample_tok_aligned_sent.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_morph_sample_tok_aligned_sent.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment} -m

    # # TR in TR template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_morph_sample_tok_aligned_sent.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment} -m
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_morph_sample_tok_aligned_sent.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned_sent/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment} -m

    # EN in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment} -m
    
    # EN in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment} -m
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment} -m
done