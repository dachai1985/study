import logging

# 设置logger名称
logger = logging.getLogger("log_demo")
# 设置log级别
logger.setLevel(logging.DEBUG)
# 创建handler
fh_stream = logging.StreamHandler()
# 写入文件
fh_file = logging.FileHandler("./test.log")
# 设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)
# 定义输出格式
formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
fh_stream.setFormatter(formater)
fh_file.setFormatter(formater)
# 添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)

logger.info("this is a info")
logger.debug("this is a debug")
logger.warning("this is a debug")


# # 设置配置信息
# logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# # 定义日志名称getlogger
# logger = logging.getLogger("log_demo")
# logger.info("info test")
# logger.debug("debug test")
# logger.warning("warning test")