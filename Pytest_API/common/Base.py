from Pytest_API.config.Conf import ConfigYaml
from Pytest_API.utils.MysqlUtil import Mysql

# 定义init_db
# 初始数据库信息，通过配置文件
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info['host']
    port = int(db_info['port'])
    user = db_info['user']
    password = db_info['password']
    database = db_info['database']
    charset = db_info['charset']

    conn = Mysql(host, user, password, database, charset, port)
    print(conn)
    return conn

if __name__ == '__main__':
    init_db('db_awesome')
