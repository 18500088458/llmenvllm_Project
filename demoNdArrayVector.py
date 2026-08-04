import numpy as np

#vectorization【向量化运算】

#标量与数组运算(向量化)
a = np.array([1, 2, 3])
print(a + 5, a * 2, a / 2, a ** 2)
#无需循环，不需要逐元素运算



#原装数组
ls = [1, 2, 3]
#print(ls + 5)  #原装数组不支持这种写法
#只能像下面这样
print(f"{[x + 5 for x in ls]}")
print(f"{[x * 2 for x in ls]}")
print(f"{[x / 2 for x in ls]}")
print(f"{[x ** 2 for x in ls]}")




