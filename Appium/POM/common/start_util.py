
import logging
import os
import sys
from appium.options.android import UiAutomator2Options
# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将项目根目录添加到系统路径
sys.path.append(os.path.join(current_dir, '..', '..'))
from POM.common.data_util import readYaml
from appium import webdriver

def setup():
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 
    logger = logging.getLogger(__name__)
    logger.debug(f"Root path: {rootPath}")
    path = os.path.join(rootPath, r"config\config.yaml")
    data = readYaml(path)
    logger.debug(f"Data: {data['desired_caps']}")

    # 创建参数项对象
    options = UiAutomator2Options().load_capabilities(data['desired_caps'])

    # 连接到Appium服务器
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        logger.info("Connected to Appium server")
        return driver
    except Exception as e:
        logger.error(f"Failed to connect to Appium server: {e}")
        raise