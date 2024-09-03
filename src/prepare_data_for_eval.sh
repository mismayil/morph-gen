#!/bin/bash

experiment=${1:-"v_final_default"}
shots=(1 3 5)
data_dir="../experiments/data"

for shot in "${shots[@]}"
do
    # # TR in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # # TR in TR template
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # # TR in EN template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # # TR in TR template for sentence completion
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # TR in EN template for tokenizer aligned
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/tok_aligned/btwd_default_final_morph_batch1_tok_aligned_gpt-4o.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/tok_aligned/btwd_default_final_morph_batch1_tok_aligned_gpt-4o.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in EN template for non-shuffled affix order
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns

    # TR in EN template for pp experiment
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_id_morph.json -t morph_disc_pp_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_ood_morph.json -t morph_disc_pp_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}

    # # TR in EN template for suffix1 experiments
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    
    # # TR in TR template for suffix1 experiments
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_suffix1_nonce.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # TR in EN template for no_dv experiments
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in TR template for no_dv experiments
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # FI in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/final/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/final/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/final/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/final/eval/temp_en/${experiment}

    # FI in FI template
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph.json -t morph_gen_fi -n ${shot} -o ${data_dir}/fi/final/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph.json -t morph_disc_fi -n ${shot} -o ${data_dir}/fi/final/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph_nonce.json -t morph_gen_fi -n ${shot} -o ${data_dir}/fi/final/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/final/default/finnish_default_final_morph_nonce.json -t morph_disc_fi -n ${shot} -o ${data_dir}/fi/final/eval/temp_fi/${experiment}

done

# TR in EN template for CoT
#python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_sample.json -t morph_gen_cot_en -n 1 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/sample -sp ${data_dir}/tr/btwd/final/default/shots/morph_gen_cot_en.json
#python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_sample.json -t morph_disc_cot_en -n 1 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/sample -sp ${data_dir}/tr/btwd/final/default/shots/morph_disc_cot_en.json
#python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_sample_nonce.json -t morph_gen_cot_en -n 1 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/sample -sp ${data_dir}/tr/btwd/final/default/shots/morph_gen_cot_en_nonce.json
#python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_sample_nonce.json -t morph_disc_cot_en -n 1 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/sample -sp ${data_dir}/tr/btwd/final/default/shots/morph_disc_cot_en_nonce.json

# TR in EN template for CoT (zero-shot)
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_cot_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_cot_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_cot_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_cot_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

# TR in TR template for CoT (zero-shot)
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_cot_tr -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_cot_tr -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_cot_tr -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_cot_tr -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1