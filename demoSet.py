data = [1,2,3,3,3]
unique = set(data)  # 使用set去重
print(type(unique))  # Output: <class 'set'>
print(unique)  # Output: {1, 2, 3}
print(list(unique))  # Output: <class 'set'>



a = {1,2,3}
b = {2,3,4}
print(a & b) #交集
print(a | b) #并集
print(a - b) #差集
print(a ^ b) #亦或
