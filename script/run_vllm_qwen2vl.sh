
# pip3 install vllm
# pip3 install qwen_vl_utils

# cd ~/prod/lmms-eval-public
# pip3 install -e .
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export NCCL_BLOCKING_WAIT=1
export NCCL_TIMEOUT=18000000
export NCCL_DEBUG=DEBUG

python3 -m lmms_eval \
    --model vllm \
    --model_args model_version=Qwen/Qwen2-VL-7B-Instruct,tensor_parallel_size=4 \
    --tasks land_space_hard \
    --batch_size 64 \
    --log_samples \
    --log_samples_suffix vllm \
    --output_path ./logs \
    --limit=64 \
    --output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/air_space_medium_hard/ 