import pandas as pd
import numpy as np
import openpyxl as opxl

#核心中的核心——查找
#--操作                       --语法                               --示例
#---------------------------------------------------------------------------------------
#单列                       df['列名']                            df['成绩']                                 
#多列                       df[['列1','列2']]                     df[['姓名'，'成绩']]                                 
#条件行                     df[条件]                              df[df['成绩'] > 90]
#按标签定位                  df.loc[row, col]                     df.loc['h1', '成绩']     行索引值, 列索引值；用label定位，标签切片两端包含； 
#按位置定位                  df.iloc[row_idx, col_idx]            df.iloc[0, 2]            用integer定位，切片左闭右开，与python列表一致  
#混合定位                    结合条件                              df.loc[df['成绩'] > 90, ['姓名']] 

df = pd.DataFrame({
    '姓名': ['张三','李四','王五'],
    '年龄': [18, 20, 19],
    '成绩': [98, 89, 95]    
})
print(f"dataFrame效果1：\n{df}\n")
# print(df.loc[df['成绩'] > 90, '姓名'])

# cond = df['成绩'] > 90 #条件 得到行
# print(f"混合定位:\n{df.loc[cond, '姓名']}\n")  #行 结合 后面的列——'姓名'是列

# sc = df['成绩'] #条件 得到行
# print(f"单列:\n{sc}\n")  #单列

# mc = df[['姓名','成绩']] #条件 得到行
# print(f"多列:\n{mc}\n")  #多列

# label = df.loc[0, "成绩"]
# print(f"标签定位:\n{label}\n")

# iloc = df.iloc[1, 2]
# print(f"位置定位:\n{iloc}\n")



#核心中的核心——列和缺失值的操作
#--操作                       --语法                                    --示例
#---------------------------------------------------------------------------------------------
#新增列                     键存在就修改，不存在新增                       df['是否及格'] = df['成绩'] >= 60                                                             
#删除列                   df.drop(columns=['是否及格'], inplace=True)                                
#缺失值处理1               df.isnull().sum() #统计每列缺失值个数
#缺失值处理2               df.dropna() #删除含缺失值的行
#缺失值处理3               df.fillna({'年龄':0}) #按列填充不同的指定值 ffill bfill
#缺失值处理4               df.fillna(method='ffill') #前向填充(用上一个有效值补全)

df['是否及格'] = df['成绩'] >= 90
print(f"dataFrame效果-新增列：\n{df}\n")

df.drop(columns=['是否及格'], inplace=True)
print(f"dataFrame效果-删除列'是否及格'：\n{df}\n")

print(f"dataFrame效果-统计缺失值个数'：\n{df.isnull().sum()}\n")
print(f"dataFrame效果-删除含缺失的行'：\n{df.dropna()}\n")
print(f"dataFrame效果-前向填充'：\n{df.ffill()}\n")
print(f"dataFrame效果-后向填充'：\n{df.bfill()}\n")



#核心中的核心——分组聚合
#--操作                       --语法                                    --示例
#---------------------------------------------------------------------------------------------
#聚合[aggregating]                                                                   
#sum                           求和                             
#mean                          平均 
#max                           最大 
#min                           最小
#count                         数量   
#std                           标准差
#median                        中位数

dfg = pd.DataFrame({
    '班级': ['A','B','A','A','B'],
    '成绩': [85, 76, 92, 88, 69]
})

# 按班级计算平均分/最高分/人数
dfgR = dfg.groupby('班级').agg(
    avg_score = ('成绩', 'mean'),
    max_score = ('成绩', 'max'),
    count = ('成绩', 'count'),
    std_score = ('成绩', 'std'),
    median_score = ('成绩', 'median')  
)
print(f"dataFrame效果-聚合函数'：\n{dfgR}\n")


#核心中的核心——表格合并
#--操作                       --语法                                    --示例
#---------------------------------------------------------------------------------------------
#聚合[aggregating]                                                                   
#inner                         内联                               
#left                          左联 
#right                         右联 
#outer                         外联
#concat                        按行或列拼接

df1 = pd.DataFrame({'ID':[1,2,3], '姓名':['张三','李四','王五']})
df2 = pd.DataFrame({'ID':[2,3,4], '成绩':[85,90,78]})

inner = pd.merge(df1, df2, on='ID', how='inner')
print(f"dataFrame效果-表格合并-内连接'：\n{inner}\n")
left = pd.merge(df1, df2, on='ID', how='left')
print(f"dataFrame效果-表格合并-左连接'：\n{left}\n")
outer = pd.merge(df1, df2, on='ID', how='outer')
print(f"dataFrame效果-表格合并-外连接'：\n{outer}\n")

line_Concat = pd.concat([df1, df2], axis=0) #按行堆叠
col_concat = pd.concat([df1, df2], axis=1) #按列堆叠
print(f"按行堆叠：{line_Concat}")
print(f"按列堆叠：{col_concat}")



#核心中的核心——数据导出读取
#--操作                       --语法                                    --示例
#---------------------------------------------------------------------------------------------                                                                  
#to_csv                       导出到csv                               
#read_csv                     读取csv 

#分析电商平台的用户行为数据
#需要读取csv文件/清洗缺失值/计算统计指标/按用户分组聚合/生成可视化报表

#纯用python循环处理，代码冗长且效率低下
#pandas让数据处理工作流清洗/简洁
df1 = pd.DataFrame({
    '班级': ['A','B','A','A','B'],
    '成绩': [85, 76, 92, 88, 69]
})
df1.to_csv('output.csv', index=False) 

#鸾尾花数据集
iris_df = pd.read_csv('iris.csv', encoding='utf-8')
print(f"dataFrame效果-鸾尾花数据集'：\n{iris_df.head()}") #读取前5个

#Excel(多个Sheet)
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
         
sheet1 = pd.read_excel('output.xlsx', sheet_name='Sheet1')
print(f"从output.xlsx中读取的sheet1:{sheet1}")
