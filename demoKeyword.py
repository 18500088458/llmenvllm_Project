import keyword

print(keyword.kwlist)  # 打印所有的关键字
print(f"关键字总数：{len(keyword.kwlist)}")  # 打印关键字总数

print(keyword.iskeyword("if"))  # 判断是否是关键字
print(keyword.iskeyword("for"))  # 判断是否是关键字
print(keyword.iskeyword("end"))  # 判断是否是关键字