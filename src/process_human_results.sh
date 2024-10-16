#!/bin/bash

# tr human eval 1
# python process_human_results.py -r ../experiments/outputs/human/tr/btwd/temp_en/batch1_sample10_hale \
#                                 -g ../experiments/data/tr/btwd/final/eval/temp_en/v_final_default_human/batch1_sample10

# tr human eval 2
# python process_human_results.py -r ../experiments/outputs/human/tr/btwd/temp_en/batch1_sample10_abdullatif \
#                                 -g ../experiments/data/tr/btwd/final/eval/temp_en/v_final_default_human/batch1_sample10

# # fi human eval 1
# python process_human_results.py -r ../experiments/outputs/human/fi/temp_en/sample5_annotator1 \
#                                 -g ../experiments/data/fi/v4/eval/temp_en/v_final_default_human/sample5

# # fi human eval 2
# python process_human_results.py -r ../experiments/outputs/human/fi/temp_en/sample5_annotator2 \
#                                 -g ../experiments/data/fi/v4/eval/temp_en/v_final_default_human/sample5  

# # fi human eval 4
# python process_human_results.py -r ../experiments/outputs/human/fi/temp_en/sample5_annotator4 \
#                                 -g ../experiments/data/fi/v4/eval/temp_en/v_final_default_human/sample5  

# python process_human_results.py -r ../experiments/outputs/human/fi/temp_en/sample10_annotator2 \
#                                 -g ../experiments/data/fi/v4/eval/temp_en/v_final_default_human/sample10  

python process_human_results.py -r ../experiments/outputs/human/fi/temp_en/sample10_annotator4 \
                                -g ../experiments/data/fi/v4/eval/temp_en/v_final_default_human/sample10 
                                