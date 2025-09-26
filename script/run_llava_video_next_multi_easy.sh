export HF_HOME="~/.cache/huggingface"

ports=(12365 12366 12367)
# "lmms-lab/LLaVA-Video-7B-Qwen2"
models=(    
    "lmms-lab/LLaVA-Video-7B-Qwen2"
    "lmms-lab/llava-next-qwen-32b"
)

for i in "${!models[@]}"; do
    accelerate launch --num_processes 8 --main_process_port ${ports[$i]} -m lmms_eval \
        --model llava_vid \
        --model_args pretrained=${models[$i]},conv_template=qwen_1_5,video_decode_backend=decord,max_frames_num=32,mm_spatial_pool_mode=average,mm_newline_position=grid,mm_resampler_location=after \
        --tasks land_space_easy \
        --device cuda:0,1,2,3,4,5,6,7 \
        --batch_size 1 \
        --log_samples \
        --log_samples_suffix ${models[$i]##*/} \
        --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_easy/
done
