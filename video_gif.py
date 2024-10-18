from moviepy.editor import VideoFileClip

# 输入视频文件路径列表
input_videos = ["1.mov"]
# 输出GIF文件路径列表
output_gifs = ["output1.gif"]

# 遍历所有视频文件并生成GIF
for input_video, output_gif in zip(input_videos, output_gifs):
    # 加载视频剪辑
    clip = VideoFileClip(input_video)

    # 调整尺寸（例如高度设为300像素，按比例缩放）
    clip_resized = clip.resize(height=300)

    # 将视频剪辑转换为GIF，降低FPS和颜色数
    clip_resized.write_gif(output_gif, fps=8, program='ffmpeg', colors=128)

    print(f"已保存GIF至 {output_gif}")
