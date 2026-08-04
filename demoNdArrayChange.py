import numpy as np

# arr = np.arange(12)
# print(arr)

# mat = arr.reshape(3,4)#转换为3行4lie矩阵结构
# print(mat)

# arr_flat = mat.flatten()#展平(副本)
# print(arr_flat)

# arr_T = mat.T #矩阵转置(行变列)
# print(arr_T)



#在深度学习预处理中极为常用
#Expend/Squeeze用于匹配神经网络输入所需的张量维度
arr1 = np.array([1,2,3])
print(arr1.shape)

arr_exp = np.expand_dims(arr1, axis = 0) #增加维度 在多为数组0索引增加长度为1的维度
print(arr_exp.shape)

arr_exp2 = np.expand_dims(arr1, axis = 1) #增加维度 在多为数组1索引增加长度为1的维度
print(arr_exp2.shape)

arr_sq = np.squeeze(arr_exp2) #减少维度
print(arr_sq.shape)

#视图View与副本Copy
# 浅拷贝VS深拷贝
#内存共用VS独立副本  



#数据类型变化
# arri = np.array([1.5,2.3,3.7])
# print(f"数据类型转换之前：{arri}")
# print(f"数据类型转换之后：{arri.astype(np.int32)}")



# #形状变换 reshape VS resize
# arrl = np.arange(12)
# print(arrl.shape)
# arrl = arrl.reshape(3, 4) 
# print(arrl.shape)
# arrl.resize(2, 6) #就地修改不需要赋值接受
# print(arrl.shape)
# print(arrl)

# a_flat = arrl.flatten() #副本
# print(f"a_flat:{a_flat}")
# a_flat[0] = 99
# print(f"arrl:{arrl}")

# a_ravel = arrl.ravel() #视图
# print(f"a_ravel:{a_ravel}")
# a_ravel[0] = 100
# print(f"arr1:{arrl}") #这里能看到 视图方式浅拷贝因为内存公用，会修改原数组arrl对应的值



# #行列互换
# a_swap = np.swapaxes(arrl, axis1=0, axis2=1)
# print(f"arrlSwap:{a_swap}")
# print(f"a_swap.T:{a_swap.T}")
# # arr_T = mat.T #矩阵转置(行变列)
