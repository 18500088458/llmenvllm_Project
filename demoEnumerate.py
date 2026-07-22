fruits = ["Apple","Banana","Cherry","watermelon","Grape"]

print(f"Fruits List: {fruits}")
print(f"Fruits enumerate: {enumerate(fruits)}")
print(f"Fruits enumerate: {next(enumerate(fruits))}")


# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# index, fruit被元组解码
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# 指定起始索引（排名从1开始 索引0对应排名1）
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")
