#!/bin/bash

experiment=${1:-"v_balanced"}
shots=(1 3 5)
data_dir="../experiments/data"

python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_id_morph.json -t morph_disc_pp_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}
python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_ood_morph.json -t morph_disc_pp_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}

# for shot in "${shots[@]}"
# do
    # TR in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_moprh_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}

    # # TR in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}

    # # TR in EN template (binary)
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_bin_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_bin_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}

    # # # TR in TR template (binary)
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_bin_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_bin_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}

    # # TR in EN template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}

    # # # TR in TR template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/balanced/btwd_prep_post_balanced_sample_morph_nonce.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_tr/${experiment}

    # TR in EN template for sense understanding
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense.json -t morph_gen_sense_en -n ${shot} -o ${data_dir}/tr/sense/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense.json -t morph_disc_sense_en -n ${shot} -o ${data_dir}/tr/sense/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense_nonce.json -t morph_gen_sense_en -n ${shot} -o ${data_dir}/tr/sense/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense_nonce.json -t morph_disc_sense_en -n ${shot} -o ${data_dir}/tr/sense/eval/temp_en/${experiment}

    # # TR in TR template for sense understanding
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense.json -t morph_gen_sense_tr -n ${shot} -o ${data_dir}/tr/sense/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense.json -t morph_disc_sense_tr -n ${shot} -o ${data_dir}/tr/sense/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense_nonce.json -t morph_gen_sense_tr -n ${shot} -o ${data_dir}/tr/sense/eval/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/sense/balanced/words_prep_balanced_sample_sense_nonce.json -t morph_disc_sense_tr -n ${shot} -o ${data_dir}/tr/sense/eval/temp_tr/${experiment}

    # EN in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/en/morpholex/temp_en/${experiment}
    
    # EN in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/en/morpholex/MorphoLEX_en_prep_balanced_sample_morph_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/en/morpholex/temp_tr/${experiment}

    # TR in EN template for tokenizer aligned
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned/btwd_prep_post_balanced_morph_sample_tok_aligned.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/tok_aligned/btwd_prep_post_balanced_morph_sample_tok_aligned.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/eval/temp_en/${experiment}
# done