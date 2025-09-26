#!/bin/bash

ports=(12346 12347 12348)
# "OpenGVLab/InternVL2_5-38B"
models=(
    #  "lmms-lab/LLaVA-Video-7B-Qwen2"
    "lmms-lab/llava-next-qwen-32b" 
)

tasks=(
    # "land_space_short_easy_sample"
    # "land_space_short_medium_sample"
    # "land_space_short_hard_sample"
    # "land_space_medium_easy_sample"
    # "land_space_medium_medium_sample"
    # "land_space_medium_hard_sample"
    # "land_space_long_easy_sample"
    # "land_space_long_medium_sample"
    # "land_space_long_hard_sample"    
    # "air_space_short_easy_sample"
    # "air_space_short_medium_sample"
    # "air_space_short_hard_sample"
    # "air_space_medium_easy_sample"
    # "air_space_medium_medium_sample"
    # "air_space_medium_hard_sample"
    # "air_space_long_easy_sample"
    # "air_space_long_medium_sample"
    # "air_space_long_hard_sample"
    # "water_space_short_easy_sample"
    # "water_space_short_medium_sample"
    # "water_space_short_hard_sample"
    # "water_space_medium_easy_sample"
    # "water_space_medium_medium_sample"
    "water_space_medium_hard_sample"
)
# max_frame: 32, 22

# Open-Space-Reasoning/outputs_sample/water_space_medium_hard_sample

for task in "${tasks[@]}"; do
    for i in "${!models[@]}"; do
        accelerate launch --num_processes 8 --main_process_port ${ports[$((i % ${#ports[@]}))]} -m lmms_eval \
            --model llava_vid \
            --model_args pretrained=${models[$i]},conv_template=qwen_1_5,video_decode_backend=decord,max_frames_num=22,mm_spatial_pool_mode=average,mm_newline_position=grid,mm_resampler_location=after \
            --tasks $task \
            --batch_size 1 \
            --log_samples \
            --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs_sample/$task/
    done
done
