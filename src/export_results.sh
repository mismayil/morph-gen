#!/bin/bash

# tr-en default
# python export_results.py -r ../experiments/outputs/majority/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/random/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                          -o ../experiments/latex/results-tr-en-default.tex \
#                          -f latex

# tr-tr default
# python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_tr/final/v_final_default/batch1 \
#                          -o ../experiments/latex/results-tr-tr-default.tex \
#                          -f latex

# # tr-en sent
# python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_sent/batch1 \
#                          -o ../experiments/latex/results-tr-en-context.tex \
#                          -f latex

# # tr-tr sent
# python export_results.py -r ../experiments/outputs/aya-23-8b/tr/btwd/temp_tr/final/v_final_sent/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_tr/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_tr/final/v_final_sent/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_tr/final/v_final_sent/batch1 \
#                          -o ../experiments/latex/results-tr-tr-context.tex \
#                          -f latex

# fi-en default
# python export_results.py -r ../experiments/outputs/majority/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/random/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
#                             ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
#                          -o ../experiments/latex/results-fi-en-default.tex \
#                          -f latex

# tr-en default by-affix
# python export_results.py -r ../experiments/outputs/majority/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/random/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
#                             ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
#                          -o ../experiments/latex/results-tr-en-by-affix/results-tr-en-by-affix.tex \
#                          -f latex -t by_affix

# fi-en default by-affix
python export_results.py -r ../experiments/outputs/majority/fi/temp_en/v4/v_final_default \
                            ../experiments/outputs/random/fi/temp_en/v4/v_final_default \
                            ../experiments/outputs/qwen-2.5-7b/fi/temp_en/v4/v_final_default \
                            ../experiments/outputs/qwen-2.5-32b/fi/temp_en/v4/v_final_default \
                            ../experiments/outputs/gemini-1.5-flash/fi/temp_en/v4/v_final_default \
                            ../experiments/outputs/gpt-4/fi/temp_en/v4/v_final_default \
                         -o ../experiments/latex/results-fi-en-by-affix/results-fi-en-by-affix.tex \
                         -f latex -t by_affix