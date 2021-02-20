#按severities严重级别运行用例 pytest -s -v test_allure_severity.py --allure-severities normal 代表只执行严重级别为normal的用例

#pytest 文件名 alluredir ./allureresult3 生成执行结果json文件
#allure generate ./allureresult3 -o ./allure-result json文件转换为离线和html报告 可以访问连接直接查看

import allure

@allure.severity(allure.severity_level.NORMAL)
def test_case1():
    print('用例1')

@allure.severity(allure.severity_level.CRITICAL)
def test_case2():
    print('用例2')

@allure.severity(allure.severity_level.BLOCKER)
def test_case3():
    print('用例3')
