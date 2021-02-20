#module级别：我们在使用标签的时候将scope设置为module，之后再每个测试函数和测试方法中都将前置函数名传入。
#只执行一次，并且是在传入函数名的测试用例中的第一个执行的测试用例之前执行。

import pytest

@pytest.fixture(scope='module')
def test_a():
    name='小张'
    print('姓名是%s,作用范围是module' %name)
    return name

def test_a1(test_a):
    name='小李'
    print('姓名是%s' %name)
    return name

class TestCase:
    def test_b(self, test_a):
        name = '小张'
        print('执行test_b')
    def test_c(self, test_a):
        sex = '小张'
        print('执行test_c')
