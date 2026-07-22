import sys
print(sys.path)

print("Hello World")

print("第一行")
print("第二行")

#换行1：\反斜杠换行
total= 1 + 2 + 3 + \
        4 + 5
print(total)

#换行2：括号内直接换行
fruits = ['apple', 'banana', 
          'orange']
print(fruits)

'''python变量是动态类型：赋值时就决定了类型，且之后可以改变类型'''
#动态类型
#3要素 id type value
x = 10
print(id(x), type(x), x)

y = 3.14
print(id(y), type(y), y)




