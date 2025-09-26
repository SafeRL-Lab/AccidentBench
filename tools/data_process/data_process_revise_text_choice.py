import json

input_file = '/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/hard/004_multi_spatial_id_shuffled.json'
output_file = '/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/medium/004_multi_spatial_id_shuffled.json'

left_directions = {"front-left", "back-left"}
right_directions = {"front-right", "back-right"}

new_options = ["A. left", "B. right"]

with open(input_file, 'r') as f:
    data = json.load(f)

for item in data:
    gt = item['ground_truth']
    try:
        # 适配原有选项数量不确定
        index = ord(gt) - ord('A')
        old_option = item['options'][index]
        direction_text = old_option.partition('. ')[2].strip().lower()
    except Exception as e: