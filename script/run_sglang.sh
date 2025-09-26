export HF_HOME="~/.cache/huggingface"
# pip install git+https://github.com/EvolvingLMMs-Lab/lmms-eval.git

python3 -m lmms_eval \
	--model=llava_sglang \
	--model_args=pretrained=lmms-lab/llava-next-72b,tokenizer=lmms-lab/llavanext-qwen-tokenizer,conv_template=chatml-llava,tp_size=8,parallel=8 \
	--tasks=land_space_hard \
	--batch_size=1 \
	--log_samples \
	--log_samples_suffix=llava_qwen \
	--output_path=/home/jovyan/workspace/Open-Space-Reasoning/outputs/air_space_medium_hard/  \
	--verbosity=INFO