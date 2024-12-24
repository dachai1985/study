from idlelib.pyshell import restart_line

import allure
from scripts.regsetup import description
from Pytest_API.config import Conf
from Pytest_API.config.Conf import ConfigYaml
import os
from Pytest_API.common.ExcelData import ExcelData
from Pytest_API.testcase.t_yaml.testlogin_yaml import data_list
from Pytest_API.utils.LogUtil import my_log
from Pytest_API.common import ExcelConfig
from Pytest_API.utils.RequestUtil import Request
import json
import pytest
from Pytest_API.utils.LogUtil import my_log
from Pytest_API.common import Base
from Pytest_API.utils.AssertUtil import TestAssertAPI
from Pytest_API.utils.MysqlUtil import Mysql

# 初始化测试用例文件
case_file = os.path.join("../data/", ConfigYaml().get_excel_file())
# 测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet_name()

# 获取运行用例列表
data_list = ExcelData(case_file, sheet_name)
run_list = data_list.get_run_case_list()
print(run_list)

log = my_log()

# 初始化DataConfig
data_key = ExcelConfig.DataConfig


class TestExcelCase:

    # 接口请求
    def run_api(self,request_url,request_type,params_type,params_info=None,headers=None,cookies=None):
        # 接口请求
        requests = Request()
        # params转义json
        if params_type == "json":
            params_info = json.loads(params_info)
        # 发送请求
        log.info("请求url:%s" % request_url)
        log.info("请求参数:%s" % params_info)

        if str(request_type).lower() == "post":
            log.info("请求前的headers:%s" % headers)
            response = requests.post(request_url, headers=headers, cookies=cookies, json=params_info)
        elif str(request_type).lower() == "get":
            response = requests.get(request_url, headers=headers, cookies=cookies, json=params_info)
        else:
            log.error("请求类型错误:%s" % request_type)

        log.info("Response Result:%s" % response)
        return response

    # 前置条件执行
    def run_pre_case(self,pre_case):
        # 前置条件执行代码
        request_url = ConfigYaml().get_conf_url() + pre_case[data_key.request_url]
        request_type = pre_case[data_key.request_type]
        params_type = pre_case[data_key.params_type]
        params_info = pre_case[data_key.params_info]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]

        headers = Base.json_parser(headers)
        cookies = Base.json_parser(cookies)
        log.info("前置条件内的headers:%s" % headers)
        res = self.run_api(request_url, request_type, params_type, params_info, headers, cookies)
        return res

    # 获取关联参数，并替换关联参数的值
    def get_correlation(self, headers, cookies, pre_res):
        headers_para, cookies_para = Base.params_find(headers, cookies)
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            headers = Base.params_replace(headers, headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            cookies =Base.params_replace(cookies, cookies_data)
        return headers, cookies

    # 修改方法参数
    @pytest.mark.parametrize("case_info", run_list)
    def test_excel_case(self, case_info):
        log.info("执行测试用例：%s" % case_info)

        # case_id = run_list[0][data_key.case_id]
        case_id = case_info[data_key.case_id]
        case_module = case_info[data_key.case_module]
        case_name = case_info[data_key.case_name]
        request_url = ConfigYaml().get_conf_url() + case_info[data_key.request_url]
        pre_condition = case_info[data_key.pre_condition]
        request_type = case_info[data_key.request_type]
        params_type = case_info[data_key.params_type]
        params_info = case_info[data_key.params_info]
        except_result = case_info[data_key.except_result]
        comment = case_info[data_key.comment]
        headers = case_info[data_key.headers]
        cookies = case_info[data_key.cookies]
        status_code = case_info[data_key.status_code]
        db_verify = case_info[data_key.db_verify]

        # 前置条件
        if pre_condition:
            # 前置测试用例
            pre_case = data_list.get_pre_case_list(pre_condition)
            log.info("前置条件:%s" % pre_condition)
            pre_res = self.run_pre_case(pre_case)
            # 如果有相关联参数，则替换
            log.info("替换前的headers:%s" % headers)
            headers, cookies = self.get_correlation(headers, cookies, pre_res)
            log.info("替换后的headers:%s" % headers)

        headers = Base.json_parser(headers)
        cookies = Base.json_parser(cookies)

        # if headers:
        #     headers = json.loads(headers)
        # else:
        #     headers = headers
        # if cookies:
        #     cookies = json.loads(cookies)
        # else:
        #     cookies = cookies

        res = self.run_api(request_url, request_type, params_type, params_info, headers, cookies)

        # allure报告
        allure.dynamic.feature(sheet_name)
        allure.dynamic.story(case_module)
        allure.dynamic.title(case_id+' '+case_name)
        # 构建包含HTML和内联样式的描述
        # desc = "<font color='blue'>Request URL:</font>{} <br/>" \
        #         "<font color='blue'>Request Type:</font>{} <br/>" \
        #         "<font color='blue'>Except Result:</font>{} <br/>" \
        #         "<font color='blue'>Response Result:</font>{}".format(request_url, request_type, except_result, res)

        # 构建Markdown格式的描述
        desc = f"""
        **请求URL:** {request_url}

        **请求类型:** {request_type}

        **预期结果:** {except_result}

        **响应结果:** {res}
        """

        allure.dynamic.description(desc)

        assert_util = TestAssertAPI()
        # 断言结果
        assert_util.assert_code(int(res["code"]), int(status_code))
        assert_util.asser_in_body(str(res["body"]),str(except_result))

        if db_verify:
            # 数据库验证
            # 初始化数据库，查询数据库数据
            Base.assert_db_data("db_awesome",res["body"],db_verify)
