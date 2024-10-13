import os
import re
import pyautogui
import pyperclip
import time

# 自定义排序函数，用于按章节数字排序文件
def natural_sort_key(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group()) if match else float('inf')

def send_to_gpt(content):
    # 将内容复制到剪贴板
    pyperclip.copy(content)
    
    # 等待1秒确保剪贴板准备就绪
    time.sleep(1)
    
    # 点击指定位置激活输入框（600, 840）
    activate_input_box()
    
    # 等待点击后确保输入框被激活
    time.sleep(1)
    
    # 模拟Cmd+V (在Mac上是Command+V，Windows是Ctrl+V)
    pyautogui.hotkey('command', 'v')  # 如果你在Windows上使用，则改为'ctrl'
    
    # 模拟按下回车键发送内容
    pyautogui.press('enter')

def read_and_send_files(directory, start_chapter, end_chapter, delay_between_messages=60):
    # 获取所有文件列表并按自然数字顺序排序
    files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")], key=natural_sort_key)

    # 定义开始和结束的文件名
    start_file = f"Chapter_{start_chapter}.txt"
    end_file = f"Chapter_{end_chapter}.txt"

    # 只处理从start_file到end_file范围内的文件
    process_files = False
    for file in files:
        if file == start_file:
            process_files = True
        
        if process_files:
            file_path = os.path.join(directory, file)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"正在发送 {file} 到聊天窗口...")
            send_to_gpt(content)

            # 等待1分钟，避免过快的发送触发系统限制
            time.sleep(delay_between_messages)

        if file == end_file:
            break

def activate_input_box():
    # 模拟鼠标点击 (600, 840) 位置来激活输入框
    pyautogui.click(600, 840)

# 调用脚本，发送文件（可以指定从哪个文件开始，到哪个文件结束）
# 例如：从 Chapter_1.txt 开始，读到 Chapter_80.txt 结束
read_and_send_files('10_36', start_chapter=22, end_chapter=36, delay_between_messages=60)

