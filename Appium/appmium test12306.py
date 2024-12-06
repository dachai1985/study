import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 设置终端参数项
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '14',
    'deviceName': 'OPPO Reno11 5G',
    'appPackage': 'com.MobileTicket',
    'appActivity': 'com.MobileTicket.ui.activity.WelcomeGuideActivity',
    'noReset': True,
    'skipServerInstallation': True
}

# 创建参数项对象
options = UiAutomator2Options().load_capabilities(desired_caps)

# 连接到Appium服务器
try:
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    logger.info("Connected to Appium server")
except Exception as e:
    logger.error(f"Failed to connect to Appium server: {e}")
    raise

# 设置隐式等待
driver.implicitly_wait(15)

class MyAppiumTest(unittest.TestCase):
    def setUp(self):
        # 初始化驱动程序
        self.driver = driver
        logger.info("Starting test setup")

    # def tearDown(self):
    #     # 测试结束后关闭驱动程序
    #     if self.driver:
    #         self.driver.quit()
    #         logger.info("Driver quit after test")

    def test_find_elements(self):
        try:
            time.sleep(5)

            for i in range(0, 2): #滑动2次
                #滑动操作
                screen_size = driver.get_window_size()
                print("手机屏幕尺寸：", screen_size) #获取屏幕尺寸并根据比例计算滑动起始点和结束点的位置，这样可以确保滑动操作在不同设备上都能正常工作。
                width = screen_size['width']
                height = screen_size['height']
                
                #手指向上滑动 页面向下滑动
                start_x = width*0.8
                start_y = height*0.8
                end_x = width*0.8
                end_y = height*0.2
                duration = 1000  # 滑动持续时间，单位为毫秒

                driver.swipe(start_x, start_y, end_x, end_y, duration)

                #页面向上滑动
                driver.swipe(width*0.8, height*0.2, width*0.8, height*0.8, duration)
            
            # 使用WebDriverWait和expected_conditions来实现显式等待，直到元素出现在页面上
            element_by_id = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.MobileTicket:id/ticket_home_btn_search"))
            )
            logger.info(f"Element by ID found: {element_by_id}")
            element_by_id.click()

            # driver.find_element(AppiumBy.NAME, "中转").click()
            element_tab = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("中转")')
            element_tab.click()

            # 对元素进行操作，如点击、获取文本等
            # element_by_id.click()
            # print(element_by_id.text)

            # 通过文本定位
            # element_by_text = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Your Text")'))
            # )
            # logger.info(f"Element by text found: {element_by_text}")

        except Exception as e:
            logger.error(f"Error in test_find_elements: {e}")
            raise

if __name__ == "__main__":
    # 使用unittest.TestLoader()实例化TestLoader对象
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(MyAppiumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)