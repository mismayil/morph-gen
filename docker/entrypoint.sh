#!/bin/bash

su ismayilz
cd /mnt/nlpdata1/home/ismayilz/morph-gen

${CONDA} run -n ${CONDA_ENV} python process_c4.py