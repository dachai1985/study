from Pytest_API.utils.ExcelUtil import ExcelReader
from Pytest_API.common.ExcelConfig import DataConfig

class ExcelData:
    def __init__(self, test_case_file, sheet_name):
        self.reader = ExcelReader(test_case_file, sheet_name)

    # 根据Run or not获取需要执行的用例数据
    def get_run_case_list(self):
        # 使用Excel工具类，获取结果list
        run_list = []
        for line in self.reader.read_test_data():
            if line[DataConfig().run_or_not] == "Y":
                run_list.append(line)
        return run_list

    # 获取全部的测试用例数据·
    def get_all_case_list(self):
        # 使用Excel工具类，获取结果list
        # case_list = []
        # for line in self.reader.read_test_data():
        #     case_list.append(line)

        case_list = [line for line in self.reader.read_test_data()]  # 列表推导式
        return case_list

    # 根据case_id获取用例前置条件
    def get_pre_case_list(self, pre_case_id):
        case_list= self.get_all_case_list()
        for line in case_list:
            if pre_case_id in dict(line).values():
                return line
        return None


