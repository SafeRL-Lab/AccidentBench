#!/bin/bash

ports=(12346 12347 12348)

models=(
    "Qwen/Qwen2-VL-2B-Instruct"    
    "Qwen/Qwen2-VL-7B-Instruct"
    
)
# "Qwen/Qwen2-VL-2B"
# "Qwen/Qwen2-VL-7B"

tasks=(
    # "land_space_short_easy"
    # "land_space_short_medium"
    # "land_space_short_hard"
    # "land_space_medium_easy"
    # "land_space_medium_medium"
    # "land_space_medium_hard"
    # "land_space_long_easy"
    # "land_space_long_medium"
    "land_space_long_hard"    
    "air_space_short_easy"
    "air_space_short_medium"
    "air_space_short_hard"
    "air_space_medium_easy"
    "air_space_medium_medium"
    "air_space_medium_hard"
    "air_space_long_easy"
    "air_space_long_medium"
    "air_space_long_hard"
    "water_space_short_easy"
    "water_space_short_medium"
    "water_space_short_hard"
    "water_space_medium_easy"
    "water_space_medium_medium"
    "water_space_medium_hard"
)

for task in "${tasks[@]}"; do
    for i in "${!models[@]}"; do
        model="${models[$i]}"
        port="${ports[$((i % ${#ports[@]}))]}"

        accelerate launch --num_processes=8 --main_process_port=$port -m lmms_eval \
            --model qwen2_vl \
            --model_args pretrained=$model,max_pixels=23592 \
            --tasks $task \
            --batch_size 1 \
            --log_samples \
            --log_samples_suffix reproduce \
            --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/$task/
    done
done



