import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    'platformName': 'Android',
    'deviceName': '98895a474348425836',
    'appPackage': 'io.appium.android.apis',
    'appActivity': 'io.appium.android.apis.ApiDemos'
}
#appPackage 写成了apk导致启动不了app TTTTTT......

print('start...........')

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Graphics')
el.click()

print('done...........')

'''
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "98895a474348425836"
caps["appPackage"] = "io.appium.android.apis"
caps["appActivity"] = "io.appium.android.apis.ApiDemos"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
'''