import json
import random
import string
from collections import Counter

def shuffle_temporal_causal(input_path, output_path):
    # Load the JSON file
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    labels = list(string.ascii_uppercase)  # ['A', 'B', 'C', ...]
    ground_truth_counter = Counter()

    for entry in data:
        original_options = entry['options']
        shuffled = original_options[:]
        random.shuffle(shuffled)

        # Rebuild new options
        new_options = []
        text_to_label = {}
        for idx, opt in enumerate(shuffled):
            _, text = opt.split('. ', 1)
            label = labels[idx]
            new_options.append(f"{label}. {text}")
            text_to_label[text] = label

        entry['options'] = new_options

        # Get old correct answer text
        old_label = entry['ground_truth']
        old_text = next(o for o in original_options if o.startswith(f"{old_label}. ")).split('. ', 1)[1]

        # Map to new label
        new_label = text_to_label[old_text]
        entry['ground_truth'] = new_label
        ground_truth_counter[new_label] += 1  # Count updated label

    # Write shuffled version
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Print result stats
    total = sum(ground_truth_counter.values())
    print("\n Ground Truth Label Distribution After Shuffle:")
    for label in sorted(ground_truth_counter):
        count = ground_truth_counter[label]
        ratio = count / total
        print(f"{label}: {count} ({ratio:.2%})")


if __name__ == '__main__':
    input_file = '/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/easy/004_multi_temporal_id.json'
    output_file = '/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/easy/004_multi_temporal_id_shuffled.json'
    shuffle_temporal_causal(input_file, output_file)
    print(f"\nShuffled data written to {o
