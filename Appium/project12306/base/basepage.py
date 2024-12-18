import logging
import os.path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    #构造函数 内置方法 实例化类后就会执行这个方法
    def __init__(self, driver):
        self.driver = driver
        self.logger = self.setup_logger()
    
    def setup_logger(self):
        log_file = 'appium_test.log'
        """清空日志文件"""
        if os.path.exists(log_file):
            with open(log_file, 'w') as file:
                pass # 打开立即关闭文件以清空内容

        """日志记录"""
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.DEBUG)  # 设置最低日志级别为DEBUG

        # 创建控制台处理器并设置日志级别
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建文件处理器并设置日志级别
        fh = logging.FileHandler('appium_test.log', mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建格式化器并将其添加到处理器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 将处理器添加到日志记录器
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger
    
    
    def wait_for_element(self, loc, timeout=10):
        #等待元素出现
        wait = WebDriverWait(self.driver, timeout)
        self.logger.debug(f"Waiting for element: {loc}")
        try:
            element = wait.until(EC.presence_of_element_located(loc))
            self.logger.debug(f"Element found: {loc}")
            return element
        except Exception as e:
            self.logger.error(f"Element not found: {loc}. Error: {e}")
            # raise
            return None

    def wait_and_click(self, loc, timeout=10):
        #等待元素出现并点击
        element = self.wait_for_element(loc, timeout)
        element.click()
        self.logger.debug(f"Clicked on element: {loc}")

    def input_text(self, loc, text, timeout=10):
        #清除并输入文本
        element = self.wait_for_element(loc, timeout)
        element.clear()
        element.send_keys(text)
        self.logger.debug(f"Input text '{text}' into element: {loc}")

    def swipe(self, start_x_ratio, start_y_ratio, end_x_ratio, end_y_ratio, duration=0):
        screen_size = self.driver.get_window_size()
        print("手机屏幕尺寸：", screen_size) #获取屏幕尺寸并根据比例计算滑动起始点和结束点的位置，这样可以确保滑动操作在不同设备上都能正常工作。
        width = screen_size['width']
        height = screen_size['height']
        self.driver.swipe(start_x=width*start_x_ratio, 
                            start_y=height*start_y_ratio, 
                            end_x=width*end_x_ratio, 
                            end_y=height*end_y_ratio, 
                            duration=1000)
        self.logger.debug(f"Swiped from ({start_x_ratio}, {start_y_ratio}) to ({end_x_ratio}, {end_y_ratio})")

    def tap_screen(self, x=None, y=None):
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
        if x is None or y is None:
            x = width/2
            y = height/2
        print("x============", x)
        print("y============", y)
        self.driver.tap([(x,y)])

    def show_elements(self):
        try:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//*")
            for element in elements:
                resource_id = element.get_attribute('resource-id')
                self.logger.debug(f"Element found: resource-id={resource_id}")
        except Exception as e:
            self.logger.error(f"Error occurred while showing elements: {e}")

        
    # def locator(self, loc):
    #     return self.driver.find_element(*loc)

    # def input(self, loc, value):
    #     self.locator(loc).send_keys(value)

    # def click(self, loc):
    #     self.locator(loc).click()