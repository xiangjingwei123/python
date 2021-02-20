#第二个测试方法中传入了fixtrue标签标记的函数名。
# 这样，在运行第二个测试方法之前便会运行该前置函数，另外的个函数我们未传入函数名便不会
import pytest
@pytest.fixture()
def test_fix():
    print('执行test_fixuse')
def test_fixuse1():
    print('执行test_fixuse1')

def test_fixuse2(test_fix):
    print('执行test_fixuse2') #执行test_fixuse2用例之前先执行fixture函数
