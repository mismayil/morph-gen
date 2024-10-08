#!/bin/bash

# tr-en default experiments
python export_results.py -r ../experiments/outputs/majority/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/random/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-8b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/aya-23-35b/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gemini-1.5-flash/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/gpt-4/tr/btwd/temp_en/final/v_final_default/batch1 \
                            ../experiments/outputs/human/tr/btwd/temp_en/batch1_sample5 \
                         -o ../experiments/latex/results-tr-en-default.tex \
                         -f latex
