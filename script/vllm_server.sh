vllm serve Qwen/Qwen2-VL-7B-Instruct \
    --port 8080 \
    --host 0.0.0.0 \
    --dtype bfloat16 \
    --limit-mm-per-prompt image=5,video=5 \
    --tensor-parallel-size 2