import os

'''
必坑指南
1.编码问题：读取文本文件时，务必hiding'encoding='utf-8'',否则读取中文时容易报错
2.资源泄露：始终坚持用'with open()'来处理文件
3.大文件：不要对未知大小的文件直接使用'.read()'或'.readlines()',优先用'for line in f'逐行处理，或者用chunksize指定【块大小】来处理，内存友好
'''

input_file = 'C:\\Users\\28306\\Desktop\\logfile.log2026-07-20.log'
out_file = 'error_file.log'

if not os.path.exists(input_file):
    print(f"错误：文件{input_file}不存在")
else:
    error_lines = []

    with open(input_file, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            if 'ERROR' in line:
                error_lines.append(line)

    if error_lines:
        with open(out_file, 'w', encoding='utf-8') as f_out:
            f_out.writelines(error_lines)
        print(f"分析完成，错误报告已保存至{out_file}")    
    else:
        print("未发现任何异常")

