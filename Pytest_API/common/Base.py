import subprocess
from Pytest_API.config.Conf import ConfigYaml
from Pytest_API.utils.MysqlUtil import Mysql
import json
import re
from Pytest_API.utils.LogUtil import my_log
from Pytest_API.utils.AssertUtil import TestAssertAPI
from Pytest_API.utils.EmailUtil import SendEmail

p_data = '\${(.*)}\$'
log = my_log()

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

# 定义assert_db_data
def assert_db_data(db_name, result, db_verify):
    sql = init_db(db_name)
    db_res = sql.fetchone(db_verify)
    log.info("数据库整体查询结果:%s" % db_res)
    db_verify_data = list(dict(db_res).keys())
    assert_util = TestAssertAPI()

    # 根据key获取数据库结果
    for line in db_verify_data:
        # res_line = res["body"][line]  # 接口返回数据
        res_line = result[line]  # 接口返回数据
        log.info("接口返回数据:%s" % res_line)
        res_db_line = dict(db_res)[line]  # 数据库查询结果
        log.info("数据库查询结果:%s" % res_db_line)
        assert_util.asser_body(res_line, res_db_line)

# 格式化字符，转换为json格式
def json_parser(json_str):
    json_obj = json.loads(json_str) if json_str else json_str
    return json_obj

# 匹配查找字符串${...}$ 中的字符
def res_find(data,pattern_data=p_data):
    '''
    :param data: 要查询的字符串
    :param pattern_data: 正则表达式
    :return: 匹配到的字符串
    '''
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res

# 替换字符串
def params_replace(data, replace_data, pattern_data=p_data):
    '''
    :param data: 要替换的字符串
    :param replace_data: 要替换成的字符串
    :param pattern_data: 正则表达式
    :return: 替换后的字符串
    '''
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    print("re_res=", re_res)
    if re_res:
        return re.sub(pattern, replace_data, data)
    return re_res

# 处理请求头和cookies
def params_find(headers, cookies):
    '''
    :param headers: 请求头
    :param cookies: 请求cookies
    :return: 处理后的headers和cookies
    '''
    if headers is None:
        headers = {}
    if cookies is None:
        cookies = {}

    # 确保headers和cookies是字符串类型才能使用'in'操作符
    if isinstance(headers, str) and "${" in headers:
        headers = res_find(headers)
    if isinstance(cookies, str) and "${" in cookies:
        cookies = res_find(cookies)
    return headers, cookies

# 生成allure报告
def allure_report(report_path, html_path):
    try:
        allure_cmd = "allure generate %s -o %s --clean" %(report_path, html_path)
        print(allure_cmd)
        subprocess.call(allure_cmd, shell=True)

        print(f"Allure report generated at {html_path}")

    except Exception as e:
        log.error("Allure report error:", e)
        print("Allure report error:", e)

# 发送邮件
# 发送电子邮件的函数
def send_email(subject="Test Report", content="", report_path=""):
    try:
        email_info = ConfigYaml().get_email_info()
        smtp_server = email_info['smtp_server']
        email_from = email_info['email_from']
        password = email_info['password']
        email_to = email_info['email_to']
        email = SendEmail(
            smtp_server=smtp_server,
            email_from=email_from,
            password=password,
            email_to=email_to,
            subject=subject,
            content=content,
            files=report_path)

        email.send_email()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", e)
        log.error("Email send error:", e)


if __name__ == '__main__':
    init_db('db_awesome')

    # str1 = '{"Authorization":"JWT ${token}$"}'
    # pattern = re.compile('\${(.*)}\$')
    # result = pattern.findall(str1)
    # print("result===========：%s" % result[0])
    # token = "123"
    # res = re.sub(pattern, token, str1)
    # print.info("res===========：%s" % res)