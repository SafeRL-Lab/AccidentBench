accelerate launch --num_processes=1 --main_process_port=12346 -m lmms_eval \
        --model qwen2_5_vl \
        --model_args=pretrained=Qwen/Qwen2.5-VL-7B-Instruct,max_pixels=12845056,use_flash_attention_2=False,interleave_visuals=True \
        --tasks land_space \
        --batch_size 1 \
        --log_samples \
        --output_path /pasteur2/u/xhanwang/lmms-eval/outputs/land_space_results.jsonl 
        # --log_samples