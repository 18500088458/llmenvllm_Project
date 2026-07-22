'''
    大文件处理
    核心思想
        按需读入，流式处理，绝不一次性加载整个文件内存，以降低内存压力
'''

# C:\Users\28306\Desktop\
# 按块读取，化整为零#
chunk_size = 1024*1024

with open('C:\\Users\\28306\\Desktop\\xianyu_20260719_oaid_rta_5(1).txt','r',encoding='utf-8') as f:
    while True:
            chunk = f.read(chunk_size)
            if not chunk:
                  break
            print(f"处理了{len(chunk)}个字符")