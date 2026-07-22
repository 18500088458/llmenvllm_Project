import pymysql

conn = pymysql.connect(
    host = "localhost",
    port=3306,
    user='root',
    password='yinmh900213',
    database='ai_chat_app',
    charset='utf8mb4'
)

cursor = conn.cursor()

cursor.execute("select * from users;")

results = cursor.fetchall()
for row in results:
    print(row)

user_to_find = 'alice'
#params传值 需要元组格式tuple
cursor.execute("select * from users where username = %s", (user_to_find,))
result = cursor.fetchone()
print(result)

# cursor.execute("insert into users (username, ps) values(%s, %s)", ('charlie','hashd_pwd'))
# conn.commit() #必须手动提交
# print(f"插入了{cursor.rowcount}行")

# cursor.execute("update users set username = %s where id = %s", ('charlies',2))
# conn.commit() #必须手动提交
# print(f"修改了{cursor.rowcount}行")

cursor.execute("delete from users where id = %s", (2,))
conn.commit() #必须手动提交
print(f"删除了{cursor.rowcount}行")

cursor.close()
conn.close()
