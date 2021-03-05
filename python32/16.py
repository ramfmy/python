#随机数字小游戏

'''
知识点：
1. random.randint(a,b)取值范围是：[a,b]，注意与range(a,b)的区别
   range(a,b)取值范围是[a,b-1]
2. print("恭喜你，你第%d次输入的数字与电脑的随机数字%d相等"%(i,a))用法
'''

import random

i = 1
a = random.randint(0,100)
b = int(input("请输入0-100中的一个数字\n然后来查看是否与电脑一样："))

while a!= b:
    if a > b:
        print("您第%d次输入的数字比电脑的随机数字小"%i)
    else:
        print("您第%d次输入的数字比电脑的随机数字大"%i)
    i += 1
    b = int(input("请重新输入一个0-100的数字："))
else:
    print("恭喜你，你第%d次输入的数字与电脑的随机数字%d相等"%(i,a))