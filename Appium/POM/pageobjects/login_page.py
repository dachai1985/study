

# 获取当前脚本的绝对路径
import os
import sys
import time
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将项目根目录添加到系统路径
sys.path.append(os.path.join(current_dir, '..', '..'))
from POM.base.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage): #这个类本身没有构造函数，但其父类有构造函数 参数driver
    #继承base层属性及行为+当前页面类特有的属性及行为
    #特有属性
    el_my = (AppiumBy.ID, 'com.MobileTicket:id/ticket_home_bottom_bar_mine')
    el_notlogind = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("未登录,点击去登录")')
    el_username = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("usernameinput")')
    el_password = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("passwordinput")')
    el_login = (AppiumBy.XPATH, '//android.widget.Button[@text="登录"]')

    #特有行为
    def login(self, username, password):
        self.logger.info("Starting login process...")
        
        try:
            self.wait_and_click(self.el_my)
            self.wait_and_click(self.el_notlogind)
            self.input_text(self.el_username, username)
            self.input_text(self.el_password, password)
            self.wait_and_click(self.el_login)
            self.logger.info("Login completed successfully.")
            time.sleep(30)

        except Exception as e:
            self.logger.error(f"An error occurred during login: {e}")
            raise
        