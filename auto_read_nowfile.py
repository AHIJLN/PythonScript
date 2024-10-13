#用于自动化GPT逐次复制当前的文件，再加上Prompt点击窗口并Enter的自动化脚本
import os
import re
import pyautogui
import pyperclip
import time

# 自定义排序函数，用于按章节数字排序文件
def natural_sort_key(filename):
    # 提取文件名中的数字部分，确保自然顺序排列
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group())  # 返回匹配到的数字
    return float('inf')

# 发送内容到GPT窗口
def send_to_gpt(content, file_name):
    # 预定义的文本
    predefined_text = "反思一下，你能先描述一下可能发生的情况，真正尝试去理解它，然后想出一个创造性的解决方案，要求忠于原著，请以下1个章节的每一个章节都精简为100字的内容，并梳理出时间、人物、地点、关键事件。回答要求：1章节数+名：2时间和地点：3精简为100字内容：\n\n"

    # 拼接预定义文本和文件内容
    full_content = predefined_text + f"【{file_name}】\n\n" + content
    
    # 将拼接后的内容复制到剪贴板
    pyperclip.copy(full_content)
    
    # 等待1秒确保剪贴板准备就绪
    time.sleep(1)
    
    # 激活输入框
    activate_input_box()
    
    # 等待点击后确保输入框被激活
    time.sleep(1)
    
    # 模拟Cmd+V (在Mac上是Command+V，Windows是Ctrl+V)
    pyautogui.hotkey('command', 'v')  # Windows系统改为'ctrl'
    
    # 模拟按下回车键发送内容
    pyautogui.press('enter')

# 读取文件并发送
def read_and_send_files(start_chapter, end_chapter, delay_between_messages=60):
    # 获取当前目录
    directory = os.getcwd()

    # 获取所有文件列表并按自然数字顺序排序
    files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")], key=natural_sort_key)
    
    # 打印当前目录下的txt文件
    print("发现的文件:", files)

    # 定义开始和结束的文件名
    start_file = f"第{start_chapter}章.txt"
    end_file = f"第{end_chapter}章.txt"

    print(f"开始文件: {start_file}, 结束文件: {end_file}")

    # 只处理从start_file到end_file范围内的文件
    process_files = False
    for file in files:
        print(f"正在检查文件: {file}")
        if file == start_file:
            print(f"匹配到开始文件: {file}, 开始处理")
            process_files = True
        
        if process_files:
            print(f"正在处理并发送文件: {file}")
            file_path = os.path.join(directory, file)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 发送内容并附加文件名
            send_to_gpt(content, file)

            # 等待设定的时间间隔，避免触发系统限制
            time.sleep(delay_between_messages)

        if file == end_file:
            print(f"匹配到结束文件: {file}, 停止处理")
            break

# 模拟点击激活输入框的位置 (根据你的实际情况调整坐标)
def activate_input_box():
    # 你可以尝试不同的位置来验证是否点击了正确位置
    pyautogui.click(600, 840)  # 这里是输入框的位置，需根据实际情况调整
    time.sleep(1)

# 调用脚本，发送文件
# 例如：从 nanxia.txt_part_6.txt 开始，读到 nanxia.txt_part_10.txt 结束
read_and_send_files(start_chapter=1, end_chapter=10, delay_between_messages=60)

