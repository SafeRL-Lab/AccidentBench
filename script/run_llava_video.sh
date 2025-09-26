export HF_HOME="~/.cache/huggingface"

# cd ~/workspace/Open-Space-Reasoning/LLaVA
# /home/jovyan/workspace/Open-Space-Reasoning/dev311/bin/pip install -e .
# pip install git+https://github.com/LLaVA-VL/LLaVA-NeXT.git
# pip install git+https://github.com/EvolvingLMMs-Lab/lmms-eval.git

# /home/jovyan/workspace/Open-Space-Reasoning/dev311/bin/pip install git+https://github.com/LLaVA-VL/LLaVA-NeXT.git

# lmms-lab/LLaVA-Video-7B-Qwen2
# lmms-lab/llava-next-qwen-32b

accelerate launch --num_processes 8 --main_process_port 12345 -m lmms_eval \
    --model llava_vid \
    --model_args pretrained=lmms-lab/LLaVA-Video-7B-Qwen2,conv_template=qwen_1_5,video_decode_backend=decord,max_frames_num=32,mm_spatial_pool_mode=average,mm_newline_position=grid,mm_resampler_location=after \
    --tasks land_space_hard \
    --device cuda:0,1,2,3,4,5,6,7 \
    --batch_size 1 \
    --log_samples \
    --log_samples_suffix llava_vid_7B \
    --log_samples \
    --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/water_space_short_hard/