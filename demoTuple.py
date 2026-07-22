#命名元素 类似字典【key/value】方式 或者类
#tuple 不可变性 + 内部元素为可变元素的话：该可变元素可以修改
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'score'])
s1 = Student('Alice', 20, 90)
print(s1.name, s1.age, s1.score)  # Output: Alice 20 90