import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# #练习1：创建包含“产品”/“单价”/“销量”三列的DataFrame，新增“总金额=单价*销量”列，筛选总金额>1000的行，按总金额降序排序，并输出结果。
# df = pd.DataFrame({
#     '产品': ['产品A', '产品B', '产品C', '产品D'],
#     '单价': [100, 200, 150, 300],
#     '销量': [10, 5, 8, 6]
# })
# df['总金额'] = df['单价'] * df['销量'] #新增行
# df = df[df['总金额'] > 1000]  #条件表达式
# df = df.sort_values('总金额', ascending=False) #排序-降序
# print(df)



# #练习2：按“部门”分组，分别统计每个部门的平均薪资和人数，结果按平均薪资降序排序。
# df = pd.DataFrame({
#     '部门': ['A', 'A', 'B', 'B'],
#     '薪资': [5000, 6000, 7000, 8000]
# })
# df_grouped = df.groupby('部门').agg(
#     avg_salary=('薪资', 'mean'), 
#     count=('薪资', 'count')
# )
# print(f"统计部门平均薪资和人数：\n{df_grouped}")

# df_grouped = df_grouped.sort_values('avg_salary', ascending=False)
# print(f"统计部门平均薪资和人数按平均薪资倒叙排序：\n{df_grouped}")



#练习3：读取一个CSV文件，检查并填充缺失值（数值列填0，字符串列填“未知”），删除完全重复的行，输出清洗后的形状
# df = pd.read_csv('sample_data.csv')
# df = df.fillna({'数值列': 0, '字符串列': '未知'})
# df = df.drop_duplicates()
# print(f"清洗后数据形状：{df.shape}")
# print(f"清洗后数据预览：\n{df.head()}")



#练习4：生成2025年1月的日期序列，创建随机访客数的Series，按周重采样计算每周方可总数并绘制折线图
# dates = pd.date_range(start='2025-01-01', end='2025-01-31', freq='D')
# visitors = pd.Series(np.random.randint(100, 500, len(dates)), index=dates)
# weekly_visitors = visitors.resample('W').sum()

# weekly_visitors.plot(kind='line', title='每周访客数', grid=True)
# plt.xlabel('日期')
# plt.ylabel('访客数')
# plt.show()



#练习5：将python生成的DataFrame（包含列：name, score）写入Mysql新表
df = pd.DataFrame({
    'name': ['张三', '李四', '王五'],   
    'score': [85, 90, 78]
})

#引擎：连接数据库2
engine = create_engine("mysql+pymysql://root:yinmh900213@localhost:3306/ai_chat_app?charset=utf8mb4", echo=False)
df.to_sql('student_scores', con=engine, if_exists='replace', index=False)
print("数据已成功写入数据库表 'student_scores'。")




