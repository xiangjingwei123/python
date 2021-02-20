import pytest
import allure

@allure.description("测试字符串相加的功能")
@allure.feature("字符串功能测试主模块")
@allure.story("字符串功能测试子模块")
@allure.issue("https://ceshiren.com/t/topic/9844/1",name='测试发现缺陷列表')
@allure.testcase("用例1：测试字符串相加结果是否正确")
@pytest.mark.parametrize("a,b",[('1','2'),('test1','test2'),('中文','中文')])

def test_add(a,b):
    print(a+b)
