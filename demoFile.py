'''文件操作就3个步骤
    1.打开
    2.读/写
    3.关闭

    with方式 自动关闭【避免了忘记关闭的问题】
'''
#config.txt是一个较小的配置文件

#1.读取了全部内容
with open('config.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
    print(content)

#按行读取
with open('data.txt', 'r', encoding = 'utf-8') as f:
    for line in f: #不占内存 
        print(line.strip())

with open('out.txt', 'w', encoding = 'utf-8') as f:
    f.write('第一行内容\n')
    f.write('第二行内容\n')
    f.write('第三行内容\n')
            



