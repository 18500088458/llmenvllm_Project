import pymysql

class DB:
    def __init__(self, host='localhost', user='root', password='', database='ai_chat_app'):
        self.config = {'host':host, 'user':user, 'password':password, 'database':database, 'charset':'utf8mb4'}

    def __enter__(self):
        self.conn = pymysql.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc, tb):
        # 退出with语句时，自动提交或回滚，并关闭链接
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.cursor.close()
        self.conn.close()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def queryOne(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchone()

    def execute(self, sql, params=None):
        return self.cursor.execute(sql, params or ())


class UserSystem:
    @staticmethod
    def register(username, password):
        with DB(password='yinmh900213') as db:
            if db.query("select id from users where username = %s", (username,)):
                print("注册失败：用户名已存在")
            else:
                db.execute("insert into users (username, ps) values(%s, %s)", (username, password))
                print("注册成功！") 
    @staticmethod
    def login(username, password):
        with DB(password='yinmh900213') as db:
            user = db.queryOne("select id from users where username =%s and ps=%s", (username, password))
            if user:
                print("登录成功")
            else:
                print("登录失败，用户名或密码错误。")    


UserSystem.register('bileah','123456')
UserSystem.login('bileah','123456')
UserSystem.login('bileah','wrongps')
