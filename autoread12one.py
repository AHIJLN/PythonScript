import os
import re
import pyautogui
import pyperclip
import time

def natural_sort_key(filename):
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group())
    return float('inf')

def send_to_gpt(content, file_name):
    predefined_text = "请将以下内容总结成一个连贯的段落，确保包含所有关键事件和细节。摘要应：1 提及主角和其他角色的事件。\n2包括关键角色事件和事物。3解释主角的行为。\n3描述其他角色与主角之间的矛盾。\n4提到主角主要变化。\n5使用连续的段落形式，不需要章节划分或标题。\n6注重主要事件的概括，省略过多的细节和背景描述。\n7简化人物的心理描写，只提及关键的情绪变化。\n8对角色之间的互动简要提及，省略详细的对话和内心独白。\n9对环境和场景的描述以概括为主，省略细节。\n10确保包含所有关键事件和细节，避免遗漏。\n11按照内容的时间顺序或事件顺序进行概括。\n请确保不遗漏任何关键细节，按照时间顺序呈现事件。\n\n"
    full_content = predefined_text + f"【{file_name}】\n\n" + content
    pyperclip.copy(full_content)
    time.sleep(1)
    activate_input_box()
    time.sleep(1)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')

def read_and_send_files(start_chapter, end_chapter, delay_between_messages=60, chapters_per_batch=12):
    directory = os.getcwd()
    files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")], key=natural_sort_key)
    print("发现的文件:", files)

    start_file = f"Chapter_{start_chapter}.txt"
    end_file = f"Chapter_{end_chapter}.txt"
    print(f"开始文件: {start_file}, 结束文件: {end_file}")

    process_files = False
    current_batch_content = ""
    file_batch = []
    batch_count = 0

    for file in files:
        print(f"正在检查文件: {file}")
        if file == start_file:
            print(f"匹配到开始文件: {file}, 开始处理")
            process_files = True
        
        if process_files:
            file_path = os.path.join(directory, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            current_batch_content += f"【{file}】\n" + content + "\n\n"
            file_batch.append(file)

            # 每12个文件作为一批发送
            if len(file_batch) == chapters_per_batch:
                print(f"发送批次 {batch_count + 1}: 文件 {file_batch}")
                send_to_gpt(current_batch_content, f"批次 {batch_count + 1}")
                
                current_batch_content = ""
                file_batch = []
                batch_count += 1
                time.sleep(delay_between_messages)

        if file == end_file:
            print(f"匹配到结束文件: {file}, 停止处理")
            break

    # 发送不足12个文件的最后一批
    if file_batch:
        print(f"发送最后批次 {batch_count + 1}: 文件 {file_batch}")
        send_to_gpt(current_batch_content, f"批次 {batch_count + 1}")
        print(f"发送了最后不足12个文件的批次 {batch_count + 1}")

def activate_input_box():
    pyautogui.click(600, 840)
    time.sleep(1)

read_and_send_files(start_chapter=13, end_chapter=36, delay_between_messages=60, chapters_per_batch=12)

