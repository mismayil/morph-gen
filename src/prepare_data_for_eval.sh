#!/bin/bash

experiment=${1:-"v_final_default"}
shots=(1 3 5)
data_dir="../experiments/data"

# for shot in "${shots[@]}"
# do
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

    # TR in EN template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in TR template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_sent_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # TR in EN template for tokenizer aligned
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/tok_aligned/btwd_default_final_morph_batch1_tok_aligned_gpt-4o.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/tok_aligned/btwd_default_final_morph_batch1_tok_aligned_gpt-4o.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in EN template for non-shuffled affix order
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -ns

    # TR in EN template for no_dv_neg
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_neg.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_neg_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in TR template for no_dv_neg
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_neg.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_no_dv_neg_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # TR in EN template for random_neg
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_random_neg.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_random_neg_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # TR in TR template for random_neg
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_random_neg.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_random_neg_nonce.json -t morph_disc_tr -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_tr/${experiment}/batch1

    # # TR in EN template for no affix
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_no_affix_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
    # python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_no_affix_en -n ${shot} -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

    # # FI in EN template
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}

    # # FI in FI template
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}

    # # FI in EN template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_sent_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_sent_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}

    # # FI in FI template for sentence completion
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_sent_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_sent_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_sent_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_sent_fi -n ${shot} -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}

    # # FI in EN template for non-shuffled affix order
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment} -ns
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment} -ns
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment} -ns
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment} -ns

    # FI in EN template for random_neg
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_random_neg.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
    # python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_random_neg_nonce.json -t morph_disc_en -n ${shot} -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# done

# TR in EN template for CoT (5-shot)
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_cot_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -sp ${data_dir}/tr/btwd/final/default/shots/v2/morph_gen_cot_en.json
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_cot_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -sp ${data_dir}/tr/btwd/final/default/shots/v2/morph_disc_cot_en.json
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_cot_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -sp ${data_dir}/tr/btwd/final/default/shots/v2/morph_gen_cot_en_nonce.json
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_cot_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1 -sp ${data_dir}/tr/btwd/final/default/shots/v2/morph_disc_cot_en_nonce.json

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

# FI in EN template for CoT (zero-shot)
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_cot_en -n 0 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_cot_en -n 0 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_cot_en -n 0 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_cot_en -n 0 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}

# FI in FI template for CoT (zero-shot)
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_cot_fi -n 0 -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_cot_fi -n 0 -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_cot_fi -n 0 -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_cot_fi -n 0 -o ${data_dir}/fi/v4/eval/temp_fi/${experiment}

# TR in EN template for human
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_human_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_human_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_human_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
# python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_human_en -n 0 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

# FI in EN template for human
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_human_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_human_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_human_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
# python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_human_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}

# TR in alt EN template
python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_gen_alt_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1.json -t morph_disc_alt_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_gen_alt_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1
python prepare_data_for_eval.py -d ${data_dir}/tr/btwd/final/default/btwd_default_final_morph_batch1_nonce.json -t morph_disc_alt_en -n 5 -o ${data_dir}/tr/btwd/final/eval/temp_en/${experiment}/batch1

# FI in alt EN template
python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_gen_alt_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph.json -t morph_disc_alt_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_gen_alt_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}
python prepare_data_for_eval.py -d ${data_dir}/fi/v4/default/finnish_v4_default_final_morph_nonce.json -t morph_disc_alt_en -n 5 -o ${data_dir}/fi/v4/eval/temp_en/${experiment}