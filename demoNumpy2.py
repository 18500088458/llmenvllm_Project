import numpy as np

a1 = np.array(1)
print(a1)
a2 = np.array((1,2,3,4.0))
print(a2)
a3 = np.array([1,2,3,4])
print(a3)

#指定数据类型
af = np.array([1,2,3], dtype=np.float32)
print(af)
au = np.array([1.0,2.5,3.0], dtype=np.uint8)
print(au)

#常用数据类型：int32,float64，bool_，complex64[复]，str_
#常用数据类型：'f4','i4'

#结构化数组(模拟 C 结构体) U10字符串10位  u1数字8位 f4=flaot32
stu_type = np.dtype([("name", "U10"),("age","u1"),("score", "f4")])
stu_arr = np.array([("张三", 20, 90),("李四", 21, 98.5),("王五", 22, 96.5)], dtype = stu_type)
print(stu_arr["name"])
print(stu_arr["age"])
print(stu_arr["score"])

# 内存布局： order='C' (行优先，默认) 或'F'(列优先)，影响大规模计算的缓存命中率，可按需选择