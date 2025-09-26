# cd /path/to/lmms-eval
# python3 -m pip install -e .;

# python3 -m pip install transformers --upgrade;
# python3 -m pip install av sentencepiece;



# accelerate launch --num_processes 8 --main_process_port 12345 -m lmms_eval \
#     --model video_llava \
#     --tasks land_space_hard \
#     --device cuda:0,1,2,3,4,5,6,7 \
#     --batch_size 1 \
#     --log_samples \
#     --log_samples_suffix \
#     --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_easy/


TASK=$1
echo $TASK
TASK_SUFFIX="${TASK//,/_}"
echo $TASK_SUFFIX

accelerate launch --num_processes 8 --main_process_port 12345 -m lmms_eval \
    --model video_llava \
    --tasks $TASK \
    --batch_size 1 \
    --log_samples \
    --log_samples_suffix $TASK_SUFFIX \
    --output_path ./logs/
