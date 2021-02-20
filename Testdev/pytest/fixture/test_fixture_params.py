#params参数可以实现前置函数的参数化，
# 调用前置函数的测试用例可以根据前置函数不同的参数执行多次。

#在fixture标签中的params参数传入了列表类型的参数列表；
# 又在前置函数中传入了request参数；最后在测试函数中我们通过request.param来表示参数（参数列表中的每个值）
import pytest

@pytest.fixture(scope='function',params=['打开文件a','打开文件b'])
#前置函数，参数固定传request
def testparams(request):
    print(request.param) #注意request.param不带s

def test_one(testparams): #调用前置函数
    print('创建文本txt')
def test_two():
    print('创建文本sql')
