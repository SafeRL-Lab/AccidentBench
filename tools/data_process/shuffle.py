import json
import random
import string

def shuffle_temporal_causal(input_path, output_path):
    # Load the JSON file
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    labels = list(string.ascii_uppercase)  # ['A', 'B', 'C', ...]

    for entry in data: # entry is a dictionary
        original_options = entry['options']
        # Shuffle the options list
        shuffled = original_options[:]
        random.shuffle(shuffled)

        # Build new labelled options and map text → new label
        new_options = []
        text_to_label = {} # used to map text to new label
        for idx, opt in enumerate(shuffled):
            # split off the old "X. " prefix
            _, text = opt.split('. ', 1)
            label = labels[idx]
            new_options.append(f"{label}. {text}")
            text_to_label[text] = label

        entry['options'] = new_options

        # Find the original correct answer’s text
        old_label = entry['ground_truth']

        # print("original_options:", original_options)
        # print("old_label:", old_label)

        old_text = next(o for o in original_options if o.startswith(f"{old_label}. ")).split('. ', 1)[1]
        # Update ground_truth to the new label
        entry['ground_truth'] = text_to_label[old_text]

    # Write out the shuffled version
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    input_file = '/Users/shangding/Documents/paper-submission/MM-AD-Bench/haoyu/haoyu_long_0701_revise_format/004_multi_intent_id.json'
    output_file = '/Users/shangding/Documents/paper-submission/MM-AD-Be