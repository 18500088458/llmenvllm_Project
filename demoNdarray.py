import numpy as np

a1 = np.array(1)
print(a1)
a2 = np.array((1,2,3,4))
print(a2)
a3 = np.array([1,2,3,4])
print(a3)

arr_f = np.array([1,2,3], dtype=np.float32)
print(arr_f)
arr_u = np.array([1,2,3], dtype=np.uint8)
print(arr_u)

#结构化数组
stu_type = np.dtype([("name", "U10"),("age", "u1"),("score", "f4")])
stu_arr = np.array([("张三",18,89),("李四",19,90),("王五",20,93)], dtype = stu_type)
print(stu_arr)
print(stu_arr["name"])
print(stu_arr["age"])
print(stu_arr["score"])









