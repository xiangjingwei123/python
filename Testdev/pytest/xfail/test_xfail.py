#用法一：xfail用法pytest.xfail(reason='')  标记用例为xfail

import pytest
class Testcases1():
    def test_case1(self):
        pytest.xfail(reason='跳过改用例')
        print('用例1执行')
    def test_case2(self):
        print('用例2执行')

#用法二：直接作为标签标记
import pytest
@pytest.mark.xfail
class Testcases2():
    def test_case1(self):
        print('用例1执行')
    def test_case2(self):
        print('用例2执行')
