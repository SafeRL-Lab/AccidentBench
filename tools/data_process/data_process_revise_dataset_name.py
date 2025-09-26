import os

def rename_files_in_folder(folder_path):
    files = sorted(os.listdir(folder_path))  # 获取文件并排序
    index = 1

    for filename in files:
        full_path = os.path.join(folder_path, filename)

        # 跳过文件夹
        if not os.path.isfile(full_path):
            continue

        ext = os.path.splitext(filename)[1]  # 保留文件扩展名
        new_name = f"ocean_space_long_{index}{ext}"
        new_full_path = os.path.join(folder_path, new_name)

        os.rename(full_path, new_full_path)
        index += 1

    print("重命名完成")

# 用法示例
folder_path = "//Users/shangding/Downloads/Documents/Open_space_reasoning/ocean/ocean_space/long_reasoning"
rename_files_in_folder(folder_path)
