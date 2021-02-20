#如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。
import pytest
@pytest.fixture
def test_fixtures():
    a='123'
    b='456'
    return(a,b)
    print(a,b)
def test_usefixture(test_fixtures):
    a1 = test_fixtures[0]
    b1 = test_fixtures[1]
    pytest.assume(a1==test_fixtures[0])
    pytest.assume(b1==test_fixtures[1])
    print('测试完成\n'+ "a1:"+ a1 + "\nb1:"+b1)
if __name__ == "__main__":
    pytest.main('-v test_fixture2.py')