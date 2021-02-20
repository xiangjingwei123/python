#调过测试用例@pytest.mark.skipif(condition='',reason=''),reason不是必传参数
#可以调过测试用例，测试类
#跳过文件里所有用例：使用pytestmark（不可更改变量名）变量 pytestmark = pytest.mark.skipif()

import pytest
import sys

@pytest.mark.skipif(condition='2>1') #跳过test_case1用例
class Testcase1():
    def test_case1(self):
        print('执行用例1')
    def test_case2(self):
        print('执行用例2')
    def test_case3(self):
        print('执行用例3')




# 当前文件下的测试用例需要满足这个条件才能被执行，跳过整个文件下用例
pytestmark = pytest.mark.skipif(2>1, reason="需要Python3.9版本以上")

class Testcase2():
    def test_001():
        assert 1 == 1


    def test_002():
        assert 8 == 8

