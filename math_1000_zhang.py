#以「第1章」……「第数字章」为规则的拆分章节脚本
import re
import chardet

def detect_encoding(file_path):
    # 自动检测文件编码
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def split_novel(input_file, output_dir):
    # 自动检测编码
    encoding = detect_encoding(input_file)
    print(f"检测到的编码是: {encoding}")

    # 使用检测到的编码读取文件内容
    with open(input_file, 'r', encoding=encoding, errors='replace') as file:
        content = file.read()

    # 使用正则表达式匹配「第N章」的章节格式作为分隔符
    chapters = re.split(r'(第\d+章\s*)', content)

    # 确保每个章节格式正确，逐章写入文件
    for i in range(1, len(chapters), 2):
        chapter_number = chapters[i].strip()  # 章节编号，例如 "第1章"
        chapter_content = chapters[i] + chapters[i+1]  # 章节标题加内容
        chapter_filename = f"{output_dir}/{chapter_number}.txt"  # 文件名为 "第1章.txt"

        # 写入单独的txt文件，使用 UTF-8 编码保存
        with open(chapter_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(chapter_content)
        print(f"已保存 {chapter_filename}")

# 使用该函数拆分小说
split_novel('bukexueyushou.txt', '1000')

