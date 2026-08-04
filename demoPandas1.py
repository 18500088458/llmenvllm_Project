import pandas as pd
import numpy as np

# arr1 = np.array([1,2,3])
# print(arr1)

#pandas数据分析库——让表格数据操作像Excel一样优雅
s1 = pd.Series([1,2,3])
s1.name = '标题1'
print(s1)
print(f"s1.hasnans:{s1.hasnans}")
print(f"s1.values:{s1.values}")
print(f"s1.shape:{s1.shape}")
#第1列打印出来的是索引，series是列数据，显示多行

s = pd.Series([5,6,np.nan,9], index=['a','b','c','d'], name='成绩')
print(s)
print(f"s.index:{s.index}")
print(f"s.values:{s.values}")
print(f"s.dtype:{s.dtype}")
print(f"s.shape:{s.shape}")
print(f"s.hasnans:{s.hasnans}")
print(f"s.name:{s.name}")

print(f"s.iloc[0]:{s.iloc[0]}") #位置索引
print(f"s.loc['a']:{s.loc['a']}") #标签索引
print(f"s.at['a']:{s.at['a']}") #单值访问
print(f"s.at[0]:{s.iat[0]}") #单值访问
print(f"切片位置：左闭右开 s[0:2]:\n{s[0:2]}") #切片位置：左闭右开
print(f"切片标签：左右都闭 s['a':'c']:\n{s['a':'c']}") #切片标签：左右都闭

# s2 = pd.Series({'a':1,'b':2,'c':3})
# print(s2)
# #字典 键是索引
# #第1列打印出来的是索引，series是列数据，显示多行

# s3 = pd.Series([1,2,3,4], index=['row1','row2','row3','row4'], dtype='int8')
# print(s3)



