#conftest.py文件名称时固定的，pytest会自动识别该文件。放到项目的根目录下就可以全局调用了，
# 如果放到某个package下，那就在改package内有效。


import pytest
# conftest.py

@pytest.fixture(scope='session')
def testlogin():
    login = {'username':'xjw','password':'pwd'}
    print('登录用户名和密码是%s' %login)
    return login

if __name__ == '__main__':
    pytest.main(['-s', 'conftest.py'])
