#!/bin/bash

su - ismayilz
cd /mnt/nlpdata1/home/ismayilz/morph-gen/src

${CONDA} run -n ${CONDA_ENV} python process_wiki.py