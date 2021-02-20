"""
猜数字游戏
"""
while True:
    a=int(input('请输入一个数字:\n'))
    b=10
    if a>b:
        print("猜大了")
    elif a<b:
        print("猜小了")
    else:
        print("猜对了")
        break

