'''
    路径操作：跨平台兼容的基石
    核心原则：永远使用os.path.join()拼接路径，不要硬编码\或/，避免因操作系统差异导致的路径错误。
    常用方法
    ----------------------
    join(a,b)：安全拼接路径
    dirname(path)：获取目录部分
    basename(path)：获取文件名
    splitext(path)：分离名与扩展名
    exists(path)：判断路径是否存在
    isfile：判断文件
    isdir：判断目录

    跨平台通用优势：保证同一份代码再windows和linux/macOS之间无缝切换运行
'''
import os

log_dir = "my_project"
log_file = "app.log"
full_path = os.path.join(log_dir, "logs", log_file)
print(full_path)
#windows: my_project\logs\app.log   反斜杠
#linux：my_project/logs/app.log     斜杠

#当前文件目录
current_dir = os.path.dirname(__file__);
print(current_dir);

#当前目录下所有文件
files = os.listdir('.')
print(files)

# 递归遍历
for root,dirs,files in os.walk('C:\\Users\\28306\\Desktop\\Ocpx'):
    print(f"当前目录：{root}")
    print(f"子目录列表：{dirs}")
    print(f"文件列表：{files}")
            