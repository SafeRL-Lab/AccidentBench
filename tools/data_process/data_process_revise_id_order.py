import json

# 输入和输出文件路径（可以相同）
input_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/forth_investigation/all_merged_label_003.json"     # ← 替换成你的 JSON 文件路径
output_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/forth_investigation/all_merged_label_003_id.json"   # ← 可以与 input_path 相同

# 起始 ID
start_id = 1

# 加载 JSON 数据
with open(input_path, 'r') as f:
    data = json.load(f)

# 递增设置 ID
for idx, item in enumerate(data):
    item['id'] = start_id + idx

# 保存新的 JSON 文件
with open(output_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"ID updated from {start_id}, saved to: {output_path}")
