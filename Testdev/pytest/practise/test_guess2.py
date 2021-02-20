'''
计算机出一个1-100之间的随机数由人来猜
'''
import random

i=int(random.randint(1,100))
print(i)
while True:
    a=int(input('请输入一个数字:\n'))
    if a>i:
        print("猜大了")
    elif a<i:
        print("猜小了")
    else:
        print("猜对了")
        break


