#http://npm.taobao.org/mirrors/chromedriver/  先下载浏览器对应驱动放置到python安装目录


import allure
from selenium import webdriver
import time
import pytest

@pytest.mark.parametrize("testdata",['allure','pytest','unnitest'])  #测试用例数据预置
@allure.title('测试百度搜索功能')
def test_steps_case(testdata):   #定义函数，并传入测试数据
    with allure.step('step one:打开浏览器输入网址'):      #测试用例分步骤执行步骤1
        driver= webdriver.Chrome(executable_path='D:/python/python_install/chromedriver')  #指定浏览器驱动
        driver.get("https://www.baidu.com")   #传入url
    with allure.step('step two:搜索框内输入allure,并点击百度一下'):  #测试用例分步骤执行步骤2
        driver.find_element_by_id('kw').send_keys(testdata)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(5)
    with allure.step('step three:保存截图搜索结果'):   #测试用例分步骤执行步骤4
        driver.save_screenshot("./practise/reslut.png")
        allure.attach.file("./practise/reslut.png")
    with allure.step('step four:关闭浏览器'):        #测试用例分步骤执行步骤4
        driver.quit()
