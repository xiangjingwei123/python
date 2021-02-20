#fixture自动使用autouse=True
#当用例很多的时候，每次都传这个参数，会很麻烦。fixture里面有个参数autouse，
# 默认是False没开启的，可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了
#autouse设置为True，自动调用fixture功能

import pytest
@pytest.fixture(scope='function',autouse=True)
def fix():
    print('执行test_fixuse')
def test_fixuse1():
    print('执行test_fixuse1')

def test_fixuse2():
    print('执行test_fixuse2')
