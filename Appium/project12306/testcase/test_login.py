import os
from Appium.project12306.pageobjects.login_page import LoginPage  #加上上面系统路径设定后才可以正常被识别导入
import pytest

@pytest.mark.usefixtures("setup_teardown")
class TestLogin: #使用pytest时，测试类不能有自定义的 __init__ 方法，pytest会自动处理测试类的实例化。此处若继承basepage类会报错      
    @pytest.fixture(autouse=True)
    def setup_method(self, setup_teardown):
        self.driver, self.base_page = setup_teardown
    # 进行登录操作
    @pytest.mark.parametrize("username,pswd", [("13504283519","chaicai1985")])
    def test_login(self, username, pswd):
        login_page = LoginPage(driver=self.driver) #父类basepage中有构造函数参数driver，所以此处实例化需传参driver
        login_page.login(username, pswd)
        self.base_page.logger.info("Done...")

    def test_logout(self):
        login_page = LoginPage(driver=self.driver)  # 父类basepage中有构造函数参数driver，所以此处实例化需传参driver
        login_page.logout()

if __name__=='__main__':
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 运行当前目录下的测试
    pytest.main([current_dir]) #不传参则会递归地查找所有符合条件的测试文件
