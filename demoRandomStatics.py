import numpy as np

#随机数与统计
np.random.seed(42)

print(np.random.rand(3,2))

#接近为0，标准正态分布
print(np.random.randn(1000).mean())
#指定正态分布
print(np.random.normal(loc=1, scale=3, size=1000).std())
#随机整数
print(np.random.randint(10, 20, size=(2,3)))
#打乱数组——洗牌
data = np.arange(10)
np.random.shuffle(data)
print(data)

#过滤 where
print(data[data > 6])
inx = np.where(data > 5, data, 0) #三元运算
print(inx)
result = np.where(data > 5, '高','低') #三元运算
print(result)

#排序
sorted_arr = np.sort(data, axis=0)
print(f"sorted_arr:{sorted_arr}")
print(f"data:{data}")
print(f"data.sort:{data.sort()}")

