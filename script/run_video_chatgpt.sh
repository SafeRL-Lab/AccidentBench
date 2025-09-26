# cd /path/to/lmms-eval
# python3 -m pip install -e .;

# python3 -m pip install sentencepiece av;


accelerate launch --num_processes 8 --main_process_port 12345 -m lmms_eval \
    --model video_chatgpt \
    --tasks land_space_hard \
    --batch_size 1 \
    --log_samples \
    --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/air_space_long_hard/