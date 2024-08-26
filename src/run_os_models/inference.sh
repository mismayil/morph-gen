#!/bin/bash
declare -A checkpoints

echo $1

checkpoints=(["xglm"]="facebook/xglm-7.5B" \
             ["llama2"]="meta-llama/Llama-2-7b-hf" \
             ["llama3"]="meta-llama/Meta-Llama-3-8B" \
             ["bloom"]="bigscience/bloomz-7b1" \
             ["mistral7b"]="mistralai/Mistral-7B-Instruct-v0.2" \
             ["cohere"]="CohereForAI/c4ai-command-r-plus-4bit")

CHECKPOINT=${checkpoints[$1]}

echo
echo "Running inference"
echo "Checkpoint name: $1"
echo "Checkpoint: $CHECKPOINT"
echo

python3 src/inference.py --model $CHECKPOINT --token TOKEN --input INPUT --output OUTPUT