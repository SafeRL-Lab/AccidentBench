import json

input_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/hard/004_multi_intent_id_shuffled.json"
output_path = "/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/easy/004_multi_intent_id.json"

new_labels = ["A", "B", "C"]
special_text = "more than 10"

with open(input_path, 'r') as f:
    data = json.load(f)

for item in data:
    options = item["options"]
    special_opt_idx = None
    int_options = []

    # 检查“more than 10”选项
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
        # 有“more than 10”，数值均分为2段
        int_values = [v for _, v in int_options]
        min_val, max_val = min(int_values), max(int_values)
        total_range = max_val - min_val + 1
        interval = total_range // 2
        boundaries = []
        for i in range(2):
            low = min_val + i * interval
            if i == 1:
                high = max_val
            else:
                high = min_val + (i + 1) * interval - 1
            boundaries.append((low, high))
        # 构造新选项
        new_options = [
            f"{new_labels[i]}. [{low},{high}]" for i, (low, high) in enumerate(boundaries)
        ]
        # 第三个选项为“more than 10”
        new_options.append(f"{new_labels[2]}. {special_text}")

        # ground_truth 映射
        gt_label = item['ground_truth']
        gt_idx = ord(gt_label) - ord('A')
        if gt_idx == special_opt_idx:
            item['ground_truth'] = new_labels[2]
        else:
            gt_value = int(options[gt_idx].partition('. ')[2].strip())
            new_gt = None
            for i, (low, high) in enumerate(boundaries):
                if low <= gt_value <= high:
                    new_gt = new_labels[i]
                    break
            if new_gt is None:
                print(f"Warning: Value {gt_value} not in any boundary for item {item.get('id')}")
                continue
            item['ground_truth'] = new_gt

        item['options'] = new_options

    else:
        # 没有“more than 10”，三等分
        int_values = [int(opt.partition('. ')[2].strip()) for opt in options]
        min_val, max_val = min(int_values), max(int_values)
        total_range = max_val - min_val + 1
        interval = total_range // 3
        boundaries = []
        for i in range(3):
            low = min_val + i * interval
            if i == 2:
                high = max_val
            else:
                high = min_val + (i + 1) * interval - 1
            boundaries.append((low, high))
        new_options = [
            f"{new_labels[i]}. [{low},{high}]" for i, (low, high) in enumerate(boundaries)
        ]
        gt_label = item['ground_truth']
        gt_idx = ord(gt_label) - ord('A')
        gt_value = int(options[gt_idx].partition('. ')[2].strip())
        new_gt = None
        for i, (low, high) in enumerate(boundaries):
            if low <= gt_value <= high:
                new_gt = new_labels[i]
                break
        if new_gt is None:
            print(f"Warning: Value {gt_value} not in any boundary for item {item.get('id')}")
            continue
        item['ground_truth'] = new_gt
        item['options'] = new_options

with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Finished! Saved to {output_path}")
