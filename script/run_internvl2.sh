# cd /path/to/lmms-eval
# python3 -m pip install -e .;


# python3 -m pip install flash-attn --no-build-isolation
# python3 -m pip install torchvision einops timm sentencepiece



accelerate launch --num_processes 8 --main_process_port 12380 -m lmms_eval \
    --model internvl2 \
    --model_args pretrained=OpenGVLab/InternVL2-8B \
    --tasks land_space_hard \
    --batch_size 1 \
    --log_samples \
    --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_hard/