#scope="class"
#fixture为class级别的时候，如果一个class里面有多个用例，都调用了次fixture，那么此fixture只在此class前执行一次。
import pytest
@pytest.fixture(scope='class')
def test_a():
    name='小张'
    print('姓名是%s,作用范围是class' %name)
    return name

def test_a1():
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
