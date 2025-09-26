export HF_HOME="~/.cache/huggingface"

# pip install git+https://github.com/LLaVA-VL/LLaVA-NeXT.git
# pip install git+https://github.com/EvolvingLMMs-Lab/lmms-eval.git

ports=(12355 12356 12357)

models=(
    "lmms-lab/llava-onevision-qwen2-0.5b-ov"
    "lmms-lab/llava-onevision-qwen2-7b-ov"
)

for i in "${!models[@]}"; do
    accelerate launch --num_processes 8 --main_process_port ${ports[$i]} -m lmms_eval \
        --model llava_onevision \
        --model_args pretrained=${models[$i]},conv_template=qwen_1_5,device_map=auto,model_name=llava_qwen \
        --tasks land_space_medium \
        --device cuda:0,1,2,3,4,5,6,7 \
        --batch_size 1 \
        --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_medium/
done