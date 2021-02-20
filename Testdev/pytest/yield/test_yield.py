import pytest
@pytest.fixture(scope='function',autouse=True)#作用范围是function
#先构造前置函数
def yieldtest():
    print('打开浏览器')
    yield
    print('关闭浏览器')  #yield后内容相当于teardown，每个用例完成后再执行yield内容

def test_search_html():
    print('输入www.baidu.com')
def test_search_info():
    print('搜索python')

