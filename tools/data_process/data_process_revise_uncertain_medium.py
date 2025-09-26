import json

input_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/hard/004_multi_temporal_id_shuffled.json"
output_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/medium/004_multi_temporal_id_shuffled.json"


new_labels = ["A", "B", "C", "D", "E", "F"]
special_text = "more than 10"

with open(input_path, 'r') as f:
    data = json.load(f)

for item in data:
    options = item["options"]
    special_opt_idx = None
    int_options = []

    # 识别“more than 10”所在的索引和其他选项
    for idx, opt in enumerate(options):
        label, _, value = opt.partition('. ')
        if value.strip().lower() == special_text:
            special_opt_idx = idx
        else:
            try:
                int_options.append((idx, int(value.strip())))
            except Exception:
                print(f"Warning: Skipping invalid option '{opt}' in item {item.get('id')}")

    if special_opt_idx is not None:
        # 有“more than 10”，只对数值选项做5等分
        int_values = [v for _, v in int_options]
        min_val, max_val = min(int_values), max(int_values)
        total_range = max_val - min_val + 1
        interval = total_range // 5
        boundaries = []
        for i in range(5):
            low = min_val + i * interval
            if i == 4:
                high = max_val
            else:
                high = min_val + (i + 1) * interval - 1
            boundaries.append((low, high))
        # 构造5个区间选项
        new_options = [
            f"{new_labels[i]}. [{low},{high}]" for i, (low, high) in enumerate(boundaries)
        ]
        # 加上“more than 10”
        new_options.append(f"{new_labels[5]}. {special_text}")

        # ground_truth �