import os
import json
from collections import defaultdict

def count_ids_in_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return len([item for item in data if 'id' in item])
            elif isinstance(data, dict):
                return len([k for k in data if isinstance(data[k], dict) and 'id' in data[k]])
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return 0

def scan_directory(root_dir):
    stats = defaultdict(lambda: defaultdict(int))
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                reasoning_type = filename.replace('.json', '')
                full_path = os.path.join(dirpath, filename)
                folder_key = os.path.relpath(dirpath, root_dir)
                count = count_ids_in_json(full_path)
                stats[folder_key][reasoning_type] += count
    return stats

def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# === 使用示例 ===
root_folder = "OpenRBench"  # 请替换为你的目录路径
output_file = "reasoning_count_summary.json"

results = scan_directory(root_folder)

# 将 defaultdict 转换为普通 dict 后保存
save_to_json({k: dict(v) for k, v in results.items()}, output_file)

print(f"统计结果已保存到: {output_file}")
