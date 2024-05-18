#!/bin/bash

su - ismayilz
cd /mnt/nlpdata1/home/ismayilz/project-morphgen/morph-gen/src
CONDA=/home/ismayilz/.conda/condabin/conda
CONDA_ENV=morphgen

${CONDA} run -n ${CONDA_ENV} python process_wiki.py