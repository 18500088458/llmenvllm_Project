import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_excel('student.xlsx').fillna(0)

# #新增——计算总分与及格判定
# df['总分'] = df['平时成绩'] * 0.3 + df['考试成绩'] * 0.7
# df['是否及格'] = df['总分'].apply(lambda x:'及格' if x >= 60 else '不及格') #True/False的表

# #统计及格率 打印—及格率
# pass_rate = (df['是否及格'] == '及格').mean()
# print(f'及格率：{pass_rate:.2%}')

# counts = df['是否及格'].value_counts()
# counts.plot(kind='pie', autopct='%1.1f%%', explode=(0, 0.05))
# plt.title('及格率分布')
# plt.ylabel('')
# plt.savefig('pass_rate.png')
# plt.show()

# df.to_excel('处理后的成绩表.xlsx', index = False)



#替换首行列标题
df = pd.read_csv('iris.csv', names=['花瓣长','花瓣宽','花萼长','花萼宽','种类'], header=0)

print(df.info())
print(df.describe())

# print(df.groupby('种类')['花萼长'].mean())

# # 箱线图：花瓣宽度按种类分布
# df.boxplot(column='花瓣宽', by='种类')
# plt.title('不同种类的花瓣宽度分布')
# plt.suptitle('')
# plt.show()



#交叉表：花瓣宽度分箱与种类的关系
cross = pd.crosstab(
    index = pd.cut(df['花瓣宽'], bins=3), #剪切花瓣宽的数据；bins=3确定均分后的份数【3个柱子】；
    columns = df['种类'],
    margins = True
)
print(f"dataFrame效果剪切表：\n{cross}\n")

#时间序列快速上手
#--操作                       --语法                               --示例
#---------------------------------------------------------------------------------------
#单列                       df['列名']                            df['成绩']                                 
#多列                       df[['列1','列2']]                     df[['姓名'，'成绩']]                                 

dates = pd.date_range(start='2025-04-26', periods=15, freq='D')
print(dates)

# 模拟销售额
np.random.seed(0)
sales = pd.Series(np.random.randint(10, 100, 15), index = dates)

print(sales.rolling(window=7).sum()) #滚动7日求和：每天显示前7天累计
print(sales.resample('W').sum())     #按周重采样：每周合计(W-SUN)
