
import logging
import os
import sys
from appium.options.android import UiAutomator2Options
from Appium.project12306.common.data_util import readyaml
from appium import webdriver


def setup():
    rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    logger = logging.getLogger(__name__)
    logger.debug(f"Root path: {rootpath}")
    path = os.path.join(rootpath, r"config\config.yaml")
    data = readyaml(path)
    logger.debug(f"Data: {data['desired_caps']}")

    # 创建参数项对象
    options = UiAutomator2Options().load_capabilities(data['desired_caps'])

    # 连接到Appium服务器
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options) #会报弃用警告
        logger.info("Connected to Appium server")
        return driver
    except Exception as e:
        logger.error(f"Failed to connect to Appium server: {e}")
        raise