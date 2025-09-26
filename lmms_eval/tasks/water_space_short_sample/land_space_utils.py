import os
import random
import re
from pathlib import Path
from collections import defaultdict

def land_space_doc_to_visual(doc):
    # 使用配置文件中定义的 dataset_path
    dataset_path = doc.get("dataset_path", "/home/jovyan/workspace/Benchmark/water_space/short")
    video_dir = Path(dataset_path) / "videos2"
    video_path = video_dir / f"{doc['scene_name']}"
    
    # 尝试不同的视频格式
    if video_path.exists():
        return [str(video_path)]
    elif video_path.with_suffix(".MP4").exists():
        return [str(video_path.with_suffix(".MP4"))]
    elif video_path.with_suffix(".mkv").exists():
        return [str(video_path.with_suffix(".mkv"))]
    elif video_path.with_suffix(".avi").exists():
        return [str(video_path.with_suffix(".avi"))]
    else:
        raise FileNotFoundError(f"Video not found: {video_path}")

def land_space_doc_to_text(doc, lmms_eval_specific_kwargs=None):
    if lmms_eval_specific_kwargs is None:
        lmms_eval_specific_kwargs = {}
    pre_prompt = lmms_eval_specific_kwargs.get("pre_prompt", "")
    post_prompt = lmms_eval_specific_kwargs.get("post_prompt", "")
    options_text = "\n".join(doc["options"])
    return f"{pre_prompt}{doc['question']}\n{options_text}{post_prompt}"

def land_space_doc_to_choice(doc):
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

def land_space_doc_to_target(doc):
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"].index(doc["ground_truth"])

def extract_answer_letter(s):
    """
    从模型输出中提取答案字母 (A, B, C, D, E, F, G, H, I, J, K, L)
    Args:
        s: 模型输出的字符串
    Returns:
        提取出的答案字母，如果没有找到则返回空字符串
    """
    s = s.strip()
    # 移除常见的答案前缀
    answer_prefixes = [
        "The answer is",
        "The correct answer is",
        "The best answer is",
        "Answer:",
        "Option:"
    ]
    for prefix in answer_prefixes:
        s = s.replace(prefix, "")
    
    # 如果输出太长且没有找到字母，返回空字符串
    if len(s.split()) > 16 and not re.search("[ABCDEFGHIJKL]", s):
        return ""
    
    # 提取第一个出现的 A、B 或 C
    matches = re.search(r"[ABCDEFGHIJKL]", s)
    if matches is None:
        return ""
    return matches[0]

def land_space_process_results(doc, results):
    pred = results[0].strip() if isinstance(results, list) else results.strip()
    pred = extract_answer_letter(pred)
    if not pred:  # 如果没有提取到有效答案，随机选择一个
        pred = random.choice(["A", "B", "C"])
    
    gold = doc["ground_truth"].strip()
    correct = (pred == gold)
    
    # 添加更多评估维度
    data_dict = {
        "id": doc["id"],
        "reasoning_style": doc["reasoning_style"],
        "pred_answer": pred,
        "answer": gold,
        "correct": correct,
        "raw_output": results[0] if isinstance(results, list) else results  # 保存原始输出
    }
    
    return {
        "land_space_acc": data_dict
    }

def land_space_aggregate_results(results):
    evaluation_result = defaultdict(lambda: {"correct": 0, "total": 0})
    for result in results:
        reasoning_style = result["reasoning_style"]
        evaluation_result[reasoning_style]["correct"] += 1 if result["correct"] else 0
        evaluation_result[reasoning_style]["total"] += 1
    
    printable_results = {}
    total_correct = 0
    total_examples = 0
    
    # Statistics by reasoning style
    for reasoning_style, stats in evaluation_result.items():
        acc = stats["correct"] / stats["total"] if stats["total"] > 0 else 0
        printable_results[reasoning_style] = {
            "num": stats["total"],
            "acc": round(acc * 100, 2)  # Convert to percentage
        }
        total_correct += stats["correct"]
        total_examples += stats["total"]
    
    # Calculate overall accuracy
    overall_acc = total_correct / total_examples if total_examples > 0 else 0
    
    # Print detailed statistics
    print(f"\nLand Space Evaluation Results:")
    print(f"Overall Accuracy: {round(overall_acc * 100, 2)}%")
    print("\nStatistics by Reasoning Style:")
    for style, stats in printable_results.items():
        print(f"{style}: {stats['acc']}% (samples: {stats['num']})")
    
    return {
        "overall_acc": round(overall_acc * 100, 2),
        "by_reasoning_style": printable_results
    }