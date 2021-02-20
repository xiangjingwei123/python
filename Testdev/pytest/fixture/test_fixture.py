#定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，
# fixture命名不要以test开头，跟用例区分开。fixture是有返回值得，没有返回值默认为None
# 。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。

import pytest
@pytest.fixture()
def fixturefunc():
    return 'abc'
def test_fixture1(fixturefunc):
    print("我调用了{}".format(fixturefunc))
if __name__ == "__main__":
    print.main('-v test_fixture.py')



