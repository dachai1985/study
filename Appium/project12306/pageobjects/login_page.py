
import time
from Appium.project12306.base.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage): #这个类本身没有构造函数，但其父类有构造函数 参数driver
    #继承base层属性及行为+当前页面类特有的属性及行为
    #特有属性
    el_agree = (AppiumBy.ID, 'com.MobileTicket:id/permission_msg_button')
    el_image = (AppiumBy.XPATH, '//android.widget.ImageView')
    el_tiyan = (AppiumBy.ID, 'com.MobileTicket:id/btn_enter')
    el_ok = (AppiumBy.ID, 'com.MobileTicket:id/guide_ok_img_down_elder')
    el_my = (AppiumBy.ID, 'com.MobileTicket:id/ticket_home_bottom_bar_mine')
    el_not_logind = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("未登录,点击去登录")')
    el_username = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("usernameinput")')
    el_password = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("passwordinput")')
    el_login = (AppiumBy.XPATH, '//android.widget.Button[@text="登录"]')
    el_fingerprint = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("暂不开启")')
    el_member_induction = (AppiumBy.ID, 'com.MobileTicket:id/ticket_home_content_container')
    # el_name_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vmc-titlebar-inner")')
    el_name_title = (AppiumBy.XPATH, '//*[contains(@text, "点击可查看个人资料")]')
    el_logout = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("退出登录")')
    el_fingerprint_confirm = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")')
    el_back_home = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("返回")')

    # login 特有行为
    def login(self, username, password):
        self.logger.info("Starting login process...")
        
        try:
            self.handle_permission_popup()
            self.skip_onboarding()

            self.wait_and_click(self.el_my)
            self.wait_and_click(self.el_not_logind)
            self.input_text(self.el_username, username)
            self.input_text(self.el_password, password)
            self.wait_and_click(self.el_login)
            self.skip_induction()
            self.logger.info("Login completed successfully.")
            time.sleep(5)

        except Exception as e:
            self.logger.error(f"An error occurred during login: {e}")
            raise

    # logout
    def logout(self):
        try:
            self.wait_and_click(self.el_name_title)
            self.wait_and_click(self.el_logout)
            self.skip_logout()
            self.wait_and_click(self.el_back_home)
            self.logger.info("Logout completed successfully.")

        except Exception as e:
            self.logger.error(f"An error occurred during logout: {e}")
            raise

    # 以下几个方法处理各弹窗
    def handle_permission_popup(self):
        if self.wait_for_element(self.el_agree, timeout=5):
            self.logger.info("Permission popup found, click agree.")
            self.wait_and_click(self.el_agree)
    
    def skip_onboarding(self):
        if self.wait_for_element(self.el_image, timeout=5):
            self.logger.info("Onboarding images found, swiping through.")
            for i in range (0, 2):
                self.swipe(0.8,0.5,0.2,0.5,1000)
        
        if self.wait_for_element(self.el_tiyan, timeout=5):
            self.logger.info("Try it now button found, click.")
            self.wait_and_click(self.el_tiyan)

        if self.wait_for_element(self.el_ok, timeout=5):
            self.logger.info("OK button found, click.")
            self.wait_and_click(self.el_ok)

    def skip_induction(self):
        if self.wait_for_element(self.el_fingerprint, timeout=5):
            self.logger.info("Fingerprint popup found, click not enabled yet.")
            self.wait_and_click(self.el_fingerprint)

        if self.wait_for_element(self.el_member_induction, timeout=5):
            self.logger.info("Member induction popup found, click any area to skip.")
            self.tap_screen()

    def skip_logout(self):
        if self.wait_for_element(self.el_fingerprint_confirm, timeout=5):
            self.logger.info("Fingerprint confirm popup found, click cancel.")
            self.wait_and_click(self.el_fingerprint_confirm)



        

