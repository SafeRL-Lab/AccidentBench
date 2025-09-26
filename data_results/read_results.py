import os
import json

# 设置主目录
root_folder = "/home/jovyan/workspace/Open-Space-Reasoning/outputs_sample/land_space_short_hard_sample"

# 输出结果列表
output_lines = []

# 遍历所有模型子文件夹
for model_folder in os.listdir(root_folder):
    model_path = os.path.join(root_folder, model_folder)
    if not os.path.isdir(model_path):
        continue

    model_name = model_folder  # 直接以子文件夹名作为模型名

    # 搜索当前模型目录下所有包含 "results" 的 json 文件
    for file in os.listdir(model_path):
        if "results" in file and file.endswith(".json"):
            file_path = os.path.join(model_path, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"读取失败: {file_path}，错误: {e}")
                continue

            results = data.get("results", {})
            for task_key, task_data in results.items():
                acc_data = task_data.get("land_space_acc,none", {})
                if not acc_data:
                    continue

                overall = acc_data.get("overall_acc", "N/A")
                reasoning = acc_data.get("by_reasoning_style", {})
                intent_acc = reasoning.get("intent_goal_reasoning", {}).get("acc", "N/A")
                spatial_acc = reasoning.get("spatial_reasoning", {}).get("acc", "N/A")
                temporal_acc = reasoning.get("temporal_causal_reasoning", {}).get("acc", "N/A")

                output_lines.append(
                    f"\\textbf{{{model_name}}} & {overall} & {temporal_acc} & {spatial_acc} & {intent_acc} \\\\"
                )

# 保存为 LaTeX 文件
output_tex_path = os.path.join(root_folder, "model_results_table.tex")
with open(output_tex_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

# 打印部分结果以预览
print("\n".join(output_lines[:10]))
