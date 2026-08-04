import numpy as np

# a1 = np.arange(0,10,2) #类似range,返回数组[0 2 4 6 8]
# print(a1)
# a2 = np.zeros((3,4)) #3行4列
# print(a2)
# a3 = (np.ones((2,3)) * 255) #
# print(a3)
a4 = np.full((2,3), 7)  #填充
print(a4)
# a5 = np.eye((6)) #单位矩阵，对角线为1，其他为0
# print(a5)

# a6 = np.linspace(0, 10, 5) #线性等分[相差值固定]：算间隔 0-10，总共5个数字【均分5份】
# print(a6)
# a61 = np.linspace(0, 1000, 4) #线性等分[相差值固定]
# print(a61)

a7 = np.logspace(0,3,4) #对数等分[相除数固定]：括号里就是指数， 10^0 到 10^3 的4个数 
print(a7)
a71 = np.logspace(0,2,3) #对数等分[相除数固定]：括号里就是指数，10^0 到 10^4 的5个数    
print(a71)
a72 = np.logspace(0,4,5,base=2)
print(a72)

print(f"a7.shape：{a7.shape}");#结构 (4,)
print(f"a4.shape：{a4.shape}");#结构 (2，3)

print(f"a7.ndim：{a7.ndim}");#几维
print(f"a4.ndim：{a4.ndim}");#几维

print(f"a7.size：{a7.size}");#数量
print(f"a4.size：{a4.size}");#数量

print(f"a7.dtype：{a7.dtype}");#数据类型
print(f"a4.dtype：{a4.dtype}");#数据类型

print(f"a7.itemsize：{a7.itemsize}");
print(f"a4.itemsize：{a4.itemsize}");

print(f"a7.nbytes：{a7.nbytes}");#字节数 4*8
print(f"a4.nbytes：{a4.nbytes}");#字节数 6*8

# a8 = np.empty((2,3)) #未初始化（随机垃圾值）
# print(a8)
