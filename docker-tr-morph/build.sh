#!/bin/sh

docker build -f ./docker/Dockerfile --build-arg DUMMY=${1} -t ic-registry.epfl.ch/nlp/mete/project-morphgen --secret id=my_env,src=/mnt/u14157_ic_nlp_001_files_nfs/nlpdata1/home/ismayilz/.runai_env .