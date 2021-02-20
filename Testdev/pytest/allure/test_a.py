#指定目录生产json格式用例结果文件 ： 命令行模式执行 pytest -s -q --alluredir=./allureresult1
#allure查看测试报告 allure serve ./allureresult1

#
import pytest
import allure
@allure.feature("测试baidu搜索功能")
@pytest.fixture()
@allure.step("前置条件：测试打开浏览器功能")
def Test_search():
    print('打开默认浏览器')
def test_browser(Test_search):
    print('打开成功')

@allure.step("测试1：测试输入搜索内容")
def test_input():
    print('输入搜索内容')

@allure.step("测试2：点击搜索")
def test_search():
    print('点击搜索')

if __name__ == "__main__":
    pytest.main('-v ,test_a.py')

