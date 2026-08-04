from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

# df = pd.read_csv('iris.csv')

#引擎：连接数据库
engine = create_engine("mysql+pymysql://root:yinmh900213@localhost:3306/ai_chat_app?charset=utf8mb4", echo=False)

# #使用DataFrame直接将数据写入mysql
# df.to_sql('iris_data', con=engine, if_exists='replace', index=False)
# print("数据已成功写入数据库表 'iris_data'。")



df = pd.read_sql_query('SELECT * FROM iris_data where species = "setosa"', con=engine)
print(f"鸾尾花列标题数据:\n{df}\n")

df_all = pd.read_sql_table('iris_data', con=engine)
print(f"鸾尾花所有数据:\n{df_all}\n")

