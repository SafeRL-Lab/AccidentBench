export HF_HOME="~/.cache/huggingface"
# pip install git+https://github.com/EvolvingLMMs-Lab/lmms-eval.git

accelerate launch --num_processes=8 --main_process_port 12348 -m lmms_eval \
    --model aria \
    --model_args pretrained=rhymes-ai/Aria \
    --tasks land_space_hard \
    --device cuda:0,1,2,3,4,5,6,7 \
    --batch_size 1 \
    --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/air_space_long_hard/ 