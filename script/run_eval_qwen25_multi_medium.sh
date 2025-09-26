#!/bin/bash

ports=(12346 12347 12348)

models=(
    "Qwen/Qwen2.5-VL-3B-Instruct"
    "Qwen/Qwen2.5-VL-7B-Instruct"
    "Qwen/Qwen2.5-VL-32B-Instruct"
)

for i in "${!models[@]}"; do
    accelerate launch --num_processes 8 --main_process_port ${ports[$i]} -m lmms_eval \
        --model qwen2_5_vl \
        --model_args pretrained=${models[$i]},max_pixels=12845056,use_flash_attention_2=False,interleave_visuals=True \
        --tasks land_space_medium \
        --device cuda:0,1,2,3,4,5,6,7 \
        --batch_size 1 \
        --log_samples \
        --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_medium/
done


