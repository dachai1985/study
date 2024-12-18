import pytest


class TestDemo:
    # data_list = ["test1","test2"]
    data_list = [("test1","123456"),("test2","1234567")]

    # 数据参数化
    # @pytest.mark.parametrize("name", data_list)
    @pytest.mark.parametrize(("name","passwd"), data_list)
    def test_a(self, name, passwd):
        print("test_a")
        print(name, passwd)
        assert 1

if __name__=="__main__":
    pytest.main([__file__])