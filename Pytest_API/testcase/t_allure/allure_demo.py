import pytest
import  allure

@allure.feature("Feature-name level1 label")
class TestAllureDemo:
    @allure.title("Testcase-title1")
    @allure.description("Testcase-description1")
    @allure.story("Story-name level2 label1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1(self):
        print("test_1")

    @allure.title("Testcase-title2")
    @allure.description("Testcase-description2")
    @allure.story("Story-name level2 label2")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_2(self):
        print("test_2")

    @allure.title("Testcase-title3")
    @allure.description("Testcase-description3")
    @allure.story("Story-name level2 label2")
    def test_3(self):
        print("test_3")

    @pytest.mark.parametrize("arg1", ["case1", "case2"])
    def test_4(self, arg1):
        print(arg1)
        allure.dynamic.title(arg1)

if __name__ == '__main__':
    pytest.main(["-v", "-s", "allure_demo.py"])