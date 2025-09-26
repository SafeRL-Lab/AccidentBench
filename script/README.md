
<div align="center">
  <a href="https://github.com/SafeRL-Lab/Open-Space-Reasoning">
    <img src="https://github.com/SafeRL-Lab/Open-Space-Reasoning/blob/master/docs/figures/logo-m4r.png" alt="Logo" width="60%"> 
  </a>
  
<h1 align="center" style="font-size: 30px;"><strong><em>M4R</em></strong>:  Measuring Massive Multi-Modal Understanding and Reasoning in Open Space</h1>
<p align="center">
    <a href="https://arxiv.org">Paper</a>
    ·
    <a href="https://github.com/Open-Space-Reasoning">Website</a>
    ·
    <a href="https://github.com/SafeRL-Lab/Open-Space-Reasoning/">Code</a>
    ·
    <a href="https://huggingface.co/Open-Space-Reasoning">Dataset</a>
    ·
    <a href="https://github.com/SafeRL-Lab/Open-Space-Reasoning/issues">Issue</a>
  </p>
</div>


 ---

<!--<p align="center" width="80%">
<img src="https://github.com/SafeRL-Lab/Open-Space-Reasoning/blob/master/docs/figures/logo-m4r.png"  width="70%" height="70%">
</p>
# M4R: Measuring Massive Multi-Modal Understanding and Reasoning in Open Space
-->



## Installation

For development, you can install the package by cloning the repository and running the following command:
```bash
pip install uv

git clone git@github.com:SafeRL-Lab/Open-Space-Reasoning.git
cd Open-Space-Reasoning
uv venv dev
source dev/bin/activate
uv pip install -e .
uv pip install -U "qwen-vl-utils"   
```

```bash
uv venv -p python3.11.5 dev311
source dev311/bin/activate
uv pip install -e .
```




### Basic Usage

Here's a basic evaluation example:

```bash
accelerate launch --num_processes=1 --main_process_port=12346 -m lmms_eval \
        --model qwen2_5_vl \
        --model_args=pretrained=Qwen/Qwen2.5-VL-7B-Instruct,max_pixels=12845056,use_flash_attention_2=False,interleave_visuals=True \
        --tasks land_space_hard \
        --batch_size 1 \
        --log_samples \
        --output_path /pasteur2/u/xhanwang/lmms-eval/outputs/land_space_hard/
```

Modify the following examples to test more models as the above script.
> More examples can be found in [examples/models](examples/models)

**Evaluation of OpenAI-Compatible Model**

```bash
bash examples/models/openai_compatible.sh
bash examples/models/xai_grok.sh
```

**Evaluation of vLLM**

```bash
bash examples/models/vllm_qwen2vl.sh
```

**Evaluation of LLaVA-OneVision**

```bash
bash examples/models/llava_onevision.sh
```

**Evaluation of LLaMA-3.2-Vision**

```bash
bash examples/models/llama_vision.sh
```

**Evaluation of Qwen2-VL**

```bash
bash examples/models/qwen2_vl.sh
bash examples/models/qwen2_5_vl.sh
```

**Evaluation of LLaVA on MME**

If you want to test LLaVA 1.5, you will have to clone their repo from [LLaVA](https://github.com/haotian-liu/LLaVA) and

```bash
bash examples/models/llava_next.sh
```

**Evaluation with tensor parallel for bigger model (llava-next-72b)**

```bash
bash examples/models/tensor_parallel.sh
```

**Evaluation with SGLang for bigger model (llava-next-72b)**

```bash
bash examples/models/sglang.sh
```

**Evaluation with vLLM for bigger model (llava-next-72b)**

```bash
bash examples/models/vllm_qwen2vl.sh
```

**More Parameters**

```bash
python3 -m lmms_eval --help
```

**Environmental Variables**
Before running experiments and evaluations, we recommend you to export following environment variables to your environment. Some are necessary for certain tasks to run.

```bash
export OPENAI_API_KEY="<YOUR_API_KEY>"
export HF_HOME="<Path to HF cache>" 
export HF_TOKEN="<YOUR_API_KEY>"
export HF_HUB_ENABLE_HF_TRANSFER="1"
export REKA_API_KEY="<YOUR_API_KEY>"
# Other possible environment variables include 
# ANTHROPIC_API_KEY,DASHSCOPE_API_KEY etc.
```

**Common Environment Issues**

Sometimes you might encounter some common issues for example error related to httpx or protobuf. To solve these issues, you can first try

```bash
python3 -m pip install httpx==0.23.3;
python3 -m pip install protobuf==3.20;
# If you are using numpy==2.x, sometimes may causing errors
python3 -m pip install numpy==1.26;
# Someties sentencepiece are required for tokenizer to work
python3 -m pip install sentencepiece;
```

## Citation
If you find the repository useful, please cite the study
``` Bash
@article{gu2025m4r,
  title={M4R: Measuring Massive Multi-Modal Understanding and Reasoning in Open Space},
  author={Gu, Shangding and Wang, Xiaohan and Ying, Donghao and Zhao, Haoyu and Yang, Runing and Li, Boyi and Jin, Ming and Pavone, Marco and Yeung-Levy, Serena and Wang, Jun and Song, Dawn and Spanos, Costas},
  journal={Github},
  year={2025}
}
```





## Acknowledgments

We thank the contributors from [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval).
