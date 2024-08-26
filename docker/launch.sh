#!/bin/bash

MY_IMAGE="ic-registry.epfl.ch/nlp/mete/project-morphgen-base"

arg_job_prefix="project-morphgen-base"
arg_job_suffix="0"
arg_job_name="$arg_job_prefix-$arg_job_suffix"

command=$1
num_cpu=${2:-4}
num_gpu=${3:-1}

# Run this for train mode
if [ "$command" == "run" ]; then
	echo "Job [$arg_job_name]"

	runai submit $arg_job_name \
		-i $MY_IMAGE \
		--cpu $num_cpu \
		--gpu $num_gpu \
		--pvc runai-nlp-ismayilz-nlpdata1:/mnt/nlpdata1 \
		--pvc runai-nlp-ismayilz-scratch:/mnt/scratch \
		--command -- bash entrypoint.sh
	exit 0
fi

# Run this for interactive mode
if [ "$command" == "run_bash" ]; then
	echo "Job [$arg_job_name]"

	# IC RunAI
	# runai submit $arg_job_name \
	# 	-i $MY_IMAGE \
	# 	--cpu $num_cpu \
	# 	--cpu-limit $num_cpu \
	# 	--memory 64G \
	# 	--memory-limit 64G \
	# 	--gpu $num_gpu \
	# 	--pvc runai-nlp-ismayilz-nlpdata1:/mnt/nlpdata1 \
	# 	--pvc runai-nlp-ismayilz-scratch:/mnt/scratch \
	# 	--interactive \
	# 	--attach \
	# 	--command -- "/bin/bash"

	# RCP RunAI
	runai submit $arg_job_name \
		-i $MY_IMAGE \
		--cpu $num_cpu \
		--cpu-limit $num_cpu \
		--memory 64G \
		--memory-limit 64G \
		--gpu-memory 80G \
		--pvc nlp-scratch:/mnt/scratch \
		--interactive \
		--attach \
		--command -- "/bin/bash"
	exit 0
fi

if [ "$command" == "log" ]; then
	runai logs $arg_job_name -f
	exit 0
fi

if [ "$command" == "stat" ]; then
	runai describe job $arg_job_name 
	exit 0
fi

if [ "$command" == "del" ]; then
	runai delete job $arg_job_name
	exit 0
fi

if [ $? -eq 0 ]; then
	runai list job
fi
