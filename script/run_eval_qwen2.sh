


accelerate launch --num_processes=8 --main_process_port=12345 -m lmms_eval \
    --model qwen2_vl \
    --model_args=pretrained=Qwen/Qwen2-VL-2B-Instruct,max_pixels=23592 \
    --tasks land_space_medium_hard \
    --batch_size 1 --log_samples --log_samples_suffix reproduce --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_hard/

