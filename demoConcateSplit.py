import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

#vstack 上下拼 → 列数必须相同，行数随便加
#hstack 左右拼 → 行数必须相同，列数随便加

# print(f"{np.vstack((a,b))}")  #垂直 vertical
# print(f"{np.hstack((a,b.T))}") #水平 horizontal

# print(np.column_stack((a, b.T)))
# print(np.concatenate((a, b), axis=0))

# print(np.stack((a, a))) #升维 +1个维度



x = np.arange(9)
x_arr = np.split(x, 3)
print(f"x_arr:{x_arr}")

x = np.arange(8)
x2_arr = np.split(x, [3,5,6,10])
print(f"x2_arr:{x2_arr}")

#[]表示序列索引；
arr = np.array([1,2,3,4,5,6])
print(np.split(arr, 2)) #均分
print(np.split(arr, [2,4])) #在索引2，4处分割
print(np.hsplit(arr.reshape(2,3), [2])) #先重新分为2行3列，然后水平分割【在索引2的位置】
print(np.array_split(arr, 4))  #不等分

