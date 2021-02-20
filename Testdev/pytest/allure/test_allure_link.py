#issue()和testcase()其实调用的也是link()，只是link_type不一样
#必传参数 url：跳转的链接
#可选参数 name：显示在allure报告的名字，如果不传就是显示完整的链接；建议传！！不然可读性不高
#可以理解成：三个方法是一样的，我们都提供跳转链接和名字，只是链接的type不一样，最终显示出来的样式不一样而已【type不一样，样式不一样】
#更好地将链接分类【访问连接、Bug链接、测试用例链接】


import pytest
import allure
@allure.link('https://www.baidu.com/')
def test_case1():
    print('用例1')

@allure.testcase('https://www.baidu.com/')
def test_case2():
    print('用例2')

@allure.issue('问题列表')
def test_case3():
    print('用例3')

