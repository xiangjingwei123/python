import pytest


@pytest.fixture(scope='class')
def test1():
    b = '男'
    print('传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
    return b
class TestCase:
    def test3(self, test1):
        name = '男'
        print('找到name')
        assert test1 == name

    def test4(self, test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex
