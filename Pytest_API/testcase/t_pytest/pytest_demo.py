import pytest

# 创建测试方法
def func(x):
    return x+1
# 使用pytest断言的方法
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_a():
    assert func(3) == 4

def test_b():
    assert func(2) == 3

def test_c():
    a = "hello"
    b = "hello world"
    assert a in b

if __name__=="__main__":
    pytest.main(["pytest_demo.py"])