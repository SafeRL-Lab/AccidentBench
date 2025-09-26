import os
import json
from collections import defaultdict

def count_ids_in_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return [item['id'] for item in data if 'id' in item]
            elif isinstance(data, dict):
                return [v['id'] for v in data.values() if isinstance(v, dict) and 'id' in v]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return []

def scan_directory(root_dir):
    stats = defaultdict(lambda: defaultdict(int))
    all_ids = []
    all_ids_nonsample = []
    all_ids_sample = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                reasoning_type = filename.replace('.json', '')
                full_path = os.path.join(dirpath, filename)
                folder_key = os.path.relpath(dirpath, root_dir)
                ids = count_ids_in_json(full_path)
                count = len(ids)

                stats[folder_key][reasoning_type] += count
                all_ids.extend(ids)

                if 'sample' in folder_key:
                    all_ids_sample.extend(ids)
                else:
                    all_ids_nonsample.extend(ids)

    return stats, all_ids, all_ids_sample, all_ids_nonsample

def compute_percent(part, total):
    return round(part / total * 100, 2) if total > 0 else 0.0

def generate_summary(stats, all_ids, all_ids_sample, all_ids_nonsample):
    total = len(all_ids)
    summary = {
        "total_ids": total,
        "total_ids_in_sample": len(all_ids_sample),
        "total_ids_outside_sample": len(all_ids_nonsample),
        "sample_percentage": compute_percent(len(all_ids_sample), total),
        "non_sample_percentage": compute_percent(len(all_ids_nonsample), total),
        "folders": {}
    }

    for folder, reasoning_dict in stats.items():
        folder_total = sum(reasoning_dict.values())
        folder_info = {
            "total_ids": folder_total,
            "percentage_of_total": compute_percent(folder_total, total),
            "reasoning_types": {}
        }

        for reasoning_type, count in reasoning_dict.items():
            folder_info["reasoning_types"][reasoning_type] = {
                "count": count,
                "percentage_of_total": compute_percent(count, total)
            }

        summary["folders"][folder] = folder_info

    return summary

def save_to_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# === 主流程 ===
root_folder = "/home/jovyan/workspace/OpenRBench"  # 请替换为你的根目录路径
output_file = "reasoning_count_with_percent.json"

stats, all_ids, all_ids_sample, all_ids_nonsample = scan_directory(root_folder)
summary = generate_summary(stats, all_ids, all_ids_sample, all_ids_nonsample)
save_to_json(summary, output_file)

print(f"统计和占比结果已保存到: {output_file}")
