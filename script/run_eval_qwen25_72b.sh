accelerate launch --num_processes=8 --main_process_port=12346 -m lmms_eval \
--model qwen2_5_vl \
--model_args=pretrained=Qwen/Qwen2.5-VL-72B-Instruct,max_pixels=12,use_flash_attention_2=False,interleave_visuals=True \
--tasks land_space_hard \
--device cuda:0,1,2,3,4,5,6,7 \
--batch_size 1 \
--log_samples \
--output_path /home/jovyan/workspace/Open-Space-Reasoning/outputs/land_space_medium_hard/

