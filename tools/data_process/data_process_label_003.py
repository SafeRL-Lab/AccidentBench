import os
import json

input_dir = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/forth_investigation/label_003"    # 替换为你的文件夹路径
output_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/forth_investigation/all_merged_label_003.json"

merged_items = []

# 读取目录下所有json文件
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        with open(os.path.join(input_dir, filename), 'r') as f:
            items = json.load(f)
            # items 应该是 list，每个元素是 dict
            merged_items.extend(items)

# 写入到文件，每行为一个json对象（无[]，非严格json格式）
with open(output_path, 'w') as f:
    for obj in merged_items:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')

print(f"合并完成，每行为一个json对象，保存在 {output_path}")
