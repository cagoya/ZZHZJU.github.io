def process_file_gbk_latin1_roundtrip(file_path):
    # 第一步：以二进制读取原始文件内容（GBK 编码的 bytes）
    with open(file_path, 'rb') as f:
        gbk_bytes = f.read()
    print("Step 1 - 原始GBK字节流：", gbk_bytes)

    # 第二步：用 Latin1 解码这段 bytes（不改变字节，只映射到字符）
    latin1_str = gbk_bytes.decode('latin1')
    print("Step 2 - Latin1 解码后的字符串：", latin1_str)

    # 第三步：再从 Latin1 字符串编码回 bytes（实际上恢复原始字节）
    recovered_bytes = latin1_str.encode('latin1')
    print("Step 3 - Latin1 编码回字节流：", recovered_bytes)

    # 第四步：用 GBK 解码这些字节，恢复原文
    recovered_text = recovered_bytes.decode('gbk')
    print("Step 4 - 恢复后的原文：", recovered_text)

# 修改为你的文件路径
process_file_gbk_latin1_roundtrip("gbk.txt")
