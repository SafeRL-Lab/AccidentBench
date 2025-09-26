pip install uv  
uv venv -p python3.11 dev311
source dev311/bin/activate
uv pip install -e .
uv pip install -U "qwen-vl-utils" 


pip install uv  
uv venv -p python3.11.5 dev3112
source dev3112/bin/activate
uv pip install -e .
uv pip install -U "qwen-vl-utils" 

source dev/bin/activate


cd Open-Space-Reasoning
uv venv dev
source dev/bin/activate
uv pip install -e .
uv pip install -U "qwen-vl-utils"  

source dev310/bin/activate


# 将 pip 显式重绑定：
# which pip
# alias pip="/home/jovyan/workspace/Open-Space-Reasoning/dev311/bin/pip"
# ~/workspace/Open-Space-Reasoning/dev311/bin/python -m pip install -e .
# ~/workspace/Open-Space-Reasoning/dev311/bin/python -m pip install -e .


pip install uv  
uv venv -p python3.10 dev310
source dev310/bin/activate
uv pip install -e .
uv pip install -U "qwen-vl-utils" 

# 安装pip
# python -m ensurepip --upgrade

