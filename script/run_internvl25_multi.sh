#!/bin/bash

ports=(12346 12347 12348)
# "OpenGVLab/InternVL2_5-38B"
models=(
    # "OpenGVLab/InternVL2_5-1B"
    # "OpenGVLab/InternVL2_5-2B"
    "OpenGVLab/InternVL2_5-4B"
    "OpenGVLab/InternVL2_5-8B"
    "OpenGVLab/InternVL2_5-26B" 
    # "OpenGVLab/InternVL2_5-38B"   
)

tasks=(
    "land_space_short_easy"
    "land_space_short_medium"
    "land_space_short_hard"
    # "land_space_medium_easy"
    # "land_space_medium_medium"
    # "land_space_medium_hard"
    # "land_space_long_easy"
    # "land_space_long_medium"
    # "land_space_long_hard"    
    # "air_space_short_easy"
    # "air_space_short_medium"
    # "air_space_short_hard"
    # "air_space_medium_easy"
    # "air_space_medium_medium"
    # "air_space_medium_hard"
    # "air_space_long_easy"
    # "air_space_long_medium"
    # "air_space_long_hard"
    # "water_space_short_easy"
    # "water_space_short_medium"
    # "water_space_short_hard"
    # "water_space_medium_easy"
    # "water_space_medium_medium"
    # "water_space_medium_hard"
)

for task in "${tasks[@]}"; do
    for i in "${!models[@]}"; do
        accelerate launch --num_processes 8 --main_process_port ${ports[$((i % ${#ports[@]}))]} -m lmms_eval \
            --model internvl2 \
            --model_args pretrained=${models[$i]},enable_chunked_prefill=True,gpu_memory_utilization=0.6,max_num_seqs=1 \
            --tasks $task \
            --batch_size 1 \
            --log_samples \
            --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/$task/
    done
done
