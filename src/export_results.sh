#!/bin/bash

# tr-en default
# python export_results.py -r ../experiments/outputs/majority/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/random/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                          -o ../experiments/latex/tr/results-tr-en-default.tex \
#                          -f latex

# fi-en default
# python export_results.py -r ../experiments/outputs/majority/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/random/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                          -o ../experiments/latex/fi/results-fi-en-default.tex \
#                          -f latex

# tr-en default by-affix
# python export_results.py -r ../experiments/outputs/majority/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/random/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                          -o ../experiments/latex/tr/results-tr-en-by-affix/results-tr-en-by-affix.tex \
#                          -f latex -t by_affix

# fi-en default by-affix
# python export_results.py -r ../experiments/outputs/majority/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/random/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                          -o ../experiments/latex/fi/results-fi-en-by-affix/results-fi-en-by-affix.tex \
#                          -f latex -t by_affix

# tr default by-lang
# python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                          -o ../experiments/latex/tr/results-tr-by-lang/results-tr-by-lang.tex \
#                          -f latex -t by_lang

# # tr-en default by-context
# python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                          -o ../experiments/latex/tr/results-tr-en-by-context/results-tr-en-by-context.tex \
#                          -f latex -t by_context


# fi default by lang
# python export_results.py -r ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_fi/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_fi/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_fi/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_fi/v4/v_final_default \
#                          -o ../experiments/latex/fi/results-fi-by-lang/results-fi-by-lang.tex \
#                          -f latex -t by_lang
   
# fi-en default by context
# python export_results.py -r ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_sent \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_sent \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_sent \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_sent \
#                          -o ../experiments/latex/fi/results-fi-en-by-context/results-fi-en-by-context.tex \
#                          -f latex -t by_context

# tr-en default by-comp
# python export_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_tok_aligned_gpt-4/batch1_sub \
#                          -o ../experiments/latex/tr/results-tr-en-by-comp/results-tr-en-by-comp.tex \
#                          -f latex -t by_comp

# tr-en default by-cot
# python export_results.py -r ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_zs_cot/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_5s_cot/batch1 \
#                          -o ../experiments/latex/tr/results-tr-en-by-cot/results-tr-en-by-cot.tex \
#                          -f latex -t by_cot

# tr-en default by-order
python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                            ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                            ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_no_shuffle/batch1 \
                         -o ../experiments/latex/tr/results-tr-en-by-order/results-tr-en-by-order.tex \
                         -f latex -t by_order


# fi-en default by-order
# python export_results.py -r ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default_no_shuffle \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default_no_shuffle \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default_no_shuffle \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default_no_shuffle \
#                          -o ../experiments/latex/fi/results-fi-en-by-order/results-fi-en-by-order.tex \
#                          -f latex -t by_order

# # tr-en default by-negsel
python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_random_neg/batch1 \
                            ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                            ../experiments/outputs/qwen-2.5-7b/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                            ../experiments/outputs/qwen-2.5-32b/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default_no_dv_neg/batch1 \
                         -o ../experiments/latex/tr/results-tr-en-by-negsel/results-tr-en-by-negsel.tex \
                         -f latex -t by_negsel