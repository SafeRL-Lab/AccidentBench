import os
import subprocess

def split_video_ffmpeg(input_video, output_dir, chunk_duration=120):
    os.makedirs(output_dir, exist_ok=True)

    # 获取视频总时长（单位：秒）
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_video
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    total_duration = float(result.stdout.strip())
    print(f"总时长: {total_duration:.2f} 秒")

    num_chunks = int(total_duration // chunk_duration) + int(total_duration % chunk_duration != 0)

    for i in range(num_chunks):
        start_time = i * chunk_duration
        output_path = os.path.join(output_dir, f"air_space_{i+1}.mp4")

        cmd = [
            "ffmpeg",
            "-ss", str(start_time),
            "-i", input_video,
            "-t", str(chunk_duration),
            "-c", "copy",
            output_path
        ]
        subprocess.run(cmd)
        print(f"Saved: {output_path}")

    print("分割完成！")

# # 示例调用
# input_video = "/path/to/your/long_video.mp4"
# output_dir = "/path/to/output"
# split_video_ffmpeg(input_video, output_dir, chunk_duration=120)


# 示例调用
input_video = "/Users/shangding/Downloads/Documents/Open_space_reasoning/drones/air_space/250_planes_in_3_hours.mp4"
output_dir = "/Users/shangding/Downloads/Documents/Open_space_reasoning/drones/air_space/250_planes_in_3_hours/"
# split_video_ffmpeg_precise(input_video, output_dir, chunk_duration=120)

split_video_ffmpeg(input_video, output_dir, chunk_duration=120)
