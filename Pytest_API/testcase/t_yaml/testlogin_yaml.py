import pytest
from Pytest_API.config import Conf
from Pytest_API.utils.YamlUtil import YamlReader
from Pytest_API.config.Conf import ConfigYaml
from Pytest_API.utils.RequestUtil import Request
import os

# 获取测试用例内容list
test_file = os.path.join(Conf.get_data_path(),'test_login.yml')
data_list = YamlReader(test_file).data_all()
print(data_list)

# 参数化执行测试用例
@pytest.mark.parametrize('login', data_list)
def test_login(login):
    # 初始化数据
    url = ConfigYaml().get_conf_url() + login['url']
    print("url=%s" %url)
    data = login['data']
    print("data=%s" %data)

    # 发送post请求
    response = Request().post(url, json=data)
    print("response=%s" %response)

if __name__ == '__main__':
    pytest.main(['-s', 'test_login_yaml.py'])