from moviepy.editor import VideoFileClip

# 输入视频文件路径列表
input_videos = ["1.mov"]
# 输出GIF文件路径列表
output_gifs = ["output1.gif"]

# 遍历所有视频文件并生成GIF
for input_video, output_gif in zip(input_videos, output_gifs):
    # 加载视频剪辑
    clip = VideoFileClip(input_video)
    
    # 将视频剪辑转换为GIF
    clip.write_gif(output_gif, fps=10, colors=256)
    print(f"已保存GIF至 {output_gif}")

