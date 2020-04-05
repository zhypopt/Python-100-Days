"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
"""

import random

print("===>猜数字游戏===>")
print("数字范围[1, 100]")

str_in = str(input("Start the game?(Y/N):"))
if "n" in str_in.lower():
    modeFlag = False
else:
    modeFlag = True
while modeFlag:
    print("===>Begin the game===>")
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer and counter <= 7:
            print('猜小了，再大一点')
        elif number > answer and counter <= 7:
            print('猜大了，再小一点')
        elif number == answer:
            print('恭喜你猜对了!')
            break
        else:
            print("You Failed! the answer is %d! " % answer)
            break
            
    str_in = str(input("Start another one?(Y/N):"))
    if "n" in str_in.lower():
        modeFlag = False
    else:
        modeFlag = True

print('===> End ===>')
    