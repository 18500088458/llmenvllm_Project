import pandas as pd
import numpy as np



#************************************************************************
#pandas的DataFrame创建与核心属性
#************************************************************************



# name_s = pd.Series(['张三','李四','王五'], name='姓名')
# age_s = pd.Series([18, 20, 19], name='年龄')
# age_s1 = pd.Series([98, 89, 95], name='成绩')
# print(name_s)
# print(age_s)
# print(age_s1)



# 我们用numpy的方式看看效果
arr = np.array({
    '姓名': ['张三','李四','王五'],
    '年龄': [18, 20, 19],
    '成绩': [98, 89, 95]    
})
print(f"numpy效果1：\n{arr}\n")

stu_type = np.dtype([("name", "U10"), ("age", "u1"), ("score", "f4")])
stu_arr = np.array([("张三", 20, 90), ("李四", 21, 98.5), ("王五", 21, 98.5)], dtype = stu_type)
print(f"numpy效果2：\n{stu_arr}\n")

#numpy的效果不好，所以直接用DataFrame更合适
print("numpy的效果不好，所以直接用DataFrame更合适")

df = pd.DataFrame({
    '姓名': ['张三','李四','王五'],
    '年龄': [18, 20, 19],
    '成绩': [98, 89, 95]    
})
print(f"dataFrame效果1：\n{df}\n")

df2 = pd.DataFrame(
    [['101', '张三', 98],['102', '李四', 95],['103', '王五', 91]],
    index=['s1','s2','s3'],
    columns=['学号','姓名','分数'])

# print(f"dataFrame效果2：\n{df2}\n")

#DataFrame详解 核心属性与方法 
# df.shape[行数,列数] 
# df.columns列名列表
# df.index获取行索引
# df.dtypes查看每列数据类型
# df.info打印DataFrame完整摘要信息
# df.describe生成数值列的统计指标

print(f"dataFrame的核心属性：\n")

print(f"df的columns:\n{df.columns}\n") 
print(f"df的index:\n{df.index}\n") 
print(f"df的dtypes:\n{df.dtypes}\n") 
print(f"df的info:\n{df.info}\n")
print(f"df的describe:\n{df.describe}\n")
print(f"--"*100)

print(f"df2的columns:\n{df2.columns}\n") 
print(f"df2的index:\n{df2.index}\n") 
print(f"df2的dtypes:\n{df2.dtypes}\n") 
print(f"df2的info:\n{df2.info}\n")
print(f"df2的describe:\n{df2.describe}\n")
print(f"--"*100)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.info)
# print(df.describe)







