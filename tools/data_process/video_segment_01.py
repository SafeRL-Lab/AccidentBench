from moviepy.editor import VideoFileClip
import os

def split_video(input_path, output_dir, chunk_duration=60):
    video = VideoFileClip(input_path)
    total_duration = int(video.duration)  # 视频总时长（秒）
    
    os.makedirs(output_dir, exist_ok=True)
    
    count = 1
    for start in range(0, total_duration, chunk_duration):
        end = min(start + chunk_duration, total_duration)
        subclip = video.subclip(start, end)
        
        output_path = os.path.join(output_dir, f"air_space_{count}.mp4")
        subclip.write_videofile(output_path, codec="libx264")
        print(f"Saved: {output_path}")
        
        count += 1

    video.close()
    print("视频分割完成")



# 示例调用
input_video = "/Users/shangding/Downloads/Documents/Open_space_reasoning/drones/air_space/250_planes_in_3_hours.mp4"
output_dir = "/Users/shangding/Downloads/Documents/Open_space_reasoning/drones/air_space/250_planes_in_3_hours/"
split_video(input_video, output_dir, chunk_duration=120)

