import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def split_novel(input_file, output_dir):
    # 自动检测编码
    encoding = detect_encoding(input_file)
    print(f"检测到的编码是: {encoding}")

    with open(input_file, 'r', encoding=encoding) as file:
        content = file.read()

    # 使用正则表达式匹配 "9." 到 "36." 的章节格式作为分隔符
    chapters = re.split(r'(\d+\.\s*)', content)

    # 如果章节格式不变，确保以数字加点号开头，逐章写入文件
    for i in range(1, len(chapters), 2):
        chapter_number = chapters[i].strip()  # 章节编号，例如 "9."
        chapter_content = chapters[i] + chapters[i+1]  # 章节标题加内容
        chapter_filename = f"{output_dir}/Chapter_{chapter_number}txt"  # 文件名

        # 写入单独的txt文件
        with open(chapter_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(chapter_content)
        print(f"已保存 {chapter_filename}")

# 使用该函数拆分小说
split_novel('bukexueyushou.txt', '1000')

