import logging
import datetime
import os
from Pytest_API.config import Conf
from Pytest_API.config.Conf import ConfigYaml

# 定义日志级别的映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}
# 封装Log工具类
class Logger:
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file # 拓展名 配置文件
        self.log_name = log_name # 参数
        self.log_level = log_level # 配置文件

        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])
        if not self.logger.handlers:
            # 输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
            fh_stream.setFormatter(formater)
            # 写入文件
            fh_file = logging.FileHandler(log_file, encoding="utf-8")
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formater)

            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)

# 初始化参数数据
# 日志文件名称，日志文件级别
# 日志文件名称 = logs目录+当前时间+扩展名
log_path = Conf.get_log_path()
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
log_extension = ConfigYaml().get_conf_log_extension()
logfile = os.path.join(log_path, current_time + log_extension)
loglevel = ConfigYaml().get_conf_log()
print(logfile)

# 对外方法，初始log工具类，提供其他类使用
def my_log(log_name = __file__):
    return Logger(log_file=logfile, log_name=log_name, log_level=loglevel).logger # 注意返回 .logger

if __name__=="__main__":
    my_log().debug("this is a debug")