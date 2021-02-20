#addfinalizer函数
import pytest
@pytest.fixture()
def myfixture(request):  #固定写法传参request
    print ("执行固件myfixture的前半部分")
    def myteardown():
        print("执行固件myfture的后半部分")
    request.addfinalizer(myteardown) #通过request.addfinalizer()的方式实现“teardown”

class Test_Pytest():
        def test_one(self,myfixture):
                print("test_one方法执行" )
                assert 1==1
        def test_two(self):
                print("test_two方法执行" )
                assert "a" in "love"
        def test_three(self):
                print("test_three方法执行" )
                assert 3-2==1

