import pytest
import allure

@allure.feature ('购物车功能')
class TestshoppingTrolley(object):
    @allure.story('加入购物车')
    def test_add_shoping_trolley(self):
        login('linda','8888')
        with allure.step("浏览商品"):
            allure.attach('商品1','三星')
            allure.attach('商品2', '华为')
        with allure.step("查看商品"):
            pass
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('期望结果', '添加购物车失败')

    @allure.story('修改购物车')
    def test_edit_shoping_trolley(self):
        pass

    @allure.story('删除购物车')
    def test_delete_shoping_trolley(self):
        pass

@allure.step('用户登录')
def login(user,pwd):
    print(user,pwd)

