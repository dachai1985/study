import pymysql
from websockets.asyncio.client import connect
from  Pytest_API.utils.LogUtil import my_log

class Mysql:
    # 连接数据库
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log = my_log()

        try:
            self.conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset=charset,
                port=port
            )
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor) # 参数为使用字典游标
        except Exception as e:
            self.log.error(f"Error while connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None

    # 获取一条数据
    def fetchone(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    # 获取全部数据
    def fetchall(self, sql,  params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    # 执行sql
    def exec(self, sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.log.error(e)
            return  False
        return True

    def __del__(self):
        # 关闭游标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    mysql = Mysql(host="localhost", user="root", password="123", database="awesome")
    # 获取一条数据
    result_one = mysql.fetchone("select * from users limit 1")
    print(result_one)
    # 获取全部数据
    result_all = mysql.fetchall("select email, passwd from users")
    print(result_all)
    # 执行sql
    result_exec = mysql.exec("update blogs set summary = 'update summary by python' where content = 'haha  happy'")
    print(result_exec)

    result_up = mysql.fetchone("select * from blogs where content = 'haha  happy'")
    print(result_up)