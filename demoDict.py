#字典：dict
s,l,t,d = "",[],(),{}
print(type(s), type(l), type(t), type(d))  # Output: <class 'str'> <class 'list'> <class 'tuple'> <class 'dict'>

student = {
    'name':'Alice',
    'age':20,
    'courses':['Math', 'Physics']
}
print(student)  # Output: Alice


student['grade'] = 'A'  # 添加新键值对
print(student)  # Output: {'name': 'Alice', 'age': 20,
student['age'] = 21  # 修改键值对
print(student)  # Output: {'name': 'Alice', 'age': 21,

#异常获取
#print(student['name1'])  # 获取键对应的值

#安全获取
print(student.get('name1','没有这个键'))  # 获取键对应的值

age = student.pop('age')  # 删除键值对并返回值
print(student)  

''' 错误删除
delbaize = student.pop('baize')  # 删除键值对并返回值
print(student)  
'''

#安全删除
del_content = student.pop('baize','没有找到baize-key')  # 删除最后一个键值对并返回元组
print(del_content)  # Output: 没有找到baize-key

print(student.keys())  # Output: dict_keys(['name', 'age', 'courses', 'grade'])
print(student.values())  # Output: dict_keys(['name', 'age', 'courses', 'grade'])
print(student.items())  # Output: dict_keys(['name', 'age', 'courses', 'grade'])


#合并于更新
d1 = {'name': 'Bob', 'age': 22}
d2 = {'sex': 1, 'grade': 'B'}
merged = d1 | d2  # 合并字典，d1和d2的键值对合并，d2的键值对会覆盖d1中相同的键
print(merged)  # Output: {'name': 'Bob', 'age': 23, 'grade': 'B'}

d1 |= d2
print(d1)  # 就地更新：后续使用频率高
print(d2)

student.clear()  # 清空字典
print(student)  # Output: {}



