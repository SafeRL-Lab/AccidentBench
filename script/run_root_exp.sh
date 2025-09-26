#!/bin/bash

# 确保脚本出错时终止
set -e

echo "Start running main.sh"

bash run_internvl2_multi.sh

bash run_internvl25_multi.sh

# bash run_eval_qwen2_multi.sh

# bash run_llava_onevision_multi_easy.sh
# bash run_llava_onevision_multi_medium.sh
# bash run_llava_onevision_multi_hard.sh

# bash run_llava_video_next_multi_easy.sh
# bash run_llava_video_next_multi_medium.sh
# bash run_llava_video_next_multi_hard.sh

# bash run_eval_qwen25_multi_easy.sh
# bash run_eval_qwen25_multi_medium.sh
# bash run_eval_qwen25_multi_hard.sh


echo "All scripts finished."
