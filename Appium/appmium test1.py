import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723/wd/hub' #url 删除/wd/hub时不行的

class TestAppinum(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def test_find_battery(self) -> None:
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
            el.click()
        except Exception as e:
            self.fail(f"Failed to find or click battery element: {e}")

if __name__=='__main__':
    unittest.main()