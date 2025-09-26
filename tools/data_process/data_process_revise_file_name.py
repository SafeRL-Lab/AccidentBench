import os

# 设置你的目标文件夹路径
# folder_path = '/Users/shangding/Downloads/Documents/Open_space_reasoning/ocean/ocean_space/mid_c_reasoning'
folder_path = '/Users/shangding/Downloads/Documents/Open_space_reasoning/drones/air_space/long_reasoning'
# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.startswith('air_space_'):
        new_filename = filename.replace('air_space_', 'air_space_long_', 1)
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')
