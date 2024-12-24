from Pytest_API.utils.LogUtil import my_log
import json

class TestAssertAPI:
    def __init__(self):
        self.log = my_log("TestAPI")

    # 验证返回状态码
    def assert_code(self, code, excepted_code):
        try:
            assert  int(code) == int(excepted_code)
            return True
        except:
            self.log.error("code error, code is %s, excepted_code is %s"%(code, excepted_code))
            raise

    # 验证返回body
    def asser_body(self, body, excepted_body):
        try:
            assert  body == excepted_body
            return True
        except:
            self.log.error("body error, body is %s, excepted_body is %s"%(body, excepted_body))
            raise

    # 验证返回body
    def asser_in_body(self, body, excepted_body):
        try:
            body = json.dumps(body) # 先将body转为json字符串
            print("body is %s\nexcepted_body is %s"%(body, excepted_body))
            assert  excepted_body in body
            return True

            # body_dict = json.loads(body)
            # excepted_body_dict = json.loads(excepted_body)
            # 检查expected_body_dict的所有键值对是否在body_dict中存在
            # assert all(item in body_dict.items() for item in excepted_body.items())

        except Exception as e:
            self.log.error("Error in body assertion: %s", e, exc_info=True)
            raise