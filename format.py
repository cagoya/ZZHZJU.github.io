import os
import re

def add_space_to_latex(text):
    """
    在所有LaTeX表达式的结尾 $ 或 $$ 前添加一个空格。

    参数:
    text (str): 包含LaTeX表达式的字符串。

    返回:
    str: 修正后的字符串。
    """
    
    # 正则表达式解释：
    # (\${1,2})  : 匹配并捕获开头的 $ 或 $$
    # (.*?)      : 匹配并捕获中间的任意字符，非贪婪模式
    # ([^ ])     : 匹配并捕获一个非空格字符，这个字符紧挨着结尾的 $ 或 $$
    # (\${1,2})  : 匹配并捕获结尾的 $ 或 $$
    #
    # 这个表达式会找到类似 `$x^2+y^2=r^2$` 或 `$$y=mx+b$$` 这样，
    # 结尾的 $ 或 $$ 前面没有空格的情况。
    
    # 需要分两步来做，防止替换时出现问题
    # 1. 匹配所有结尾没有空格的 $...$
    text = re.sub(r'(\$.*?[^\s])(\$)', r'\1 \2', text)
    
    # 2. 匹配所有结尾没有空格的 $$...$$
    text = re.sub(r'(\$\$.*?[^\s])(\$\$)', r'\1 \2', text)
    
    return text

def process_md_files_in_directory(directory_path):
    """
    递归遍历指定目录及其所有子目录下的 .md 文件，并修正其LaTeX表达式格式。

    参数:
    directory_path (str): 要处理的文件夹路径。
    """
    
    print(f"正在递归处理目录: {directory_path}")
    
    # os.walk 会生成一个三元组 (dirpath, dirnames, filenames)
    # dirpath 是当前正在遍历的目录的路径
    # dirnames 是当前目录下的所有子目录名列表
    # filenames 是当前目录下的所有文件名列表
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename) # 构建完整文件路径
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # 修正内容
                    new_content = add_space_to_latex(content)
                    
                    # 如果内容有变化，则写回文件
                    if content != new_content:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print(f"已更新文件: {file_path}")
                    else:
                        print(f"文件 {file_path} 无需修改。")
                
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")


if __name__ == "__main__":
    target_directory = "./docs"
    process_md_files_in_directory(target_directory)