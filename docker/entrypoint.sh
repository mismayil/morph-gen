#!/bin/bash

cd /mnt/nlpdata1/home/ismayilz/project-SP
export HF_DATASETS_CACHE=/mnt/nlpdata1/home/ismayilz/.cache

${CONDA} run -n ${CONDA_ENV} python process_c4.py -d /mnt/nlpdata1/share/datasets/allenai___json/en-139638ded39e9288/0.0.0/8bb11242116d547c741b2e8a1f18598ffdd40a1d4f2a2872c7a28b697434bc96 -o /mnt/nlpdata1/home/ismayilz/project-SP-data