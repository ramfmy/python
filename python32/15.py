#随机生成验证码的两种方式(数字+字母)

'''
知识点：
1. range(a,b) 取值范围是[a,b-1]
2. chr(i) 将整型i转换为ascii对应的字符
3. random.sample()函数用法：
    a. rs = random.sample(range(0, 9), 4)
       其中range(0, 9)是范围，4是随机取几个数。
       注意：
       这里，取出的数不可以重复，且输出的数要小于等于范围，也就是
       4<=9
    b. list = [0,1,2,3,4]
       rs = random.sample(list, 2)
4. join函数必须接的是字符串或者字符串列表

'''

#方法一
import random

list1 = []
for i in range(65,91):
    #通过for循环遍历ascii追加到空列表中
    list1.append(chr(i))

for j in range(97,123):
    list1.append(chr(j))

for k in range(48,58):
    list1.append(chr(k))

#print(list1)
ma = random.sample(list1, 6)
#print(ma)   #此时ma为列表
ma = ''.join(ma)  #将列表转化为字符串
print(ma)


#方法二
import random,string

str1 = "0123456789"
#string.ascii_letters 包含所有的字母（大写+小写）的字符串
str2 = string.ascii_letters
str3 = str1 + str2
#print(str3)

ma1 = random.sample(str3, 6)
ma1 = ''.join(ma1)
print(ma1)