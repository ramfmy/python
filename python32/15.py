#随机生成验证码的两种方式（数字+字母）
import random

list1 = []
for i in range(65,91):
    #通过for循环遍历asii追加到空列表中
    list1.append(chr(i))

for j in range(97,123):
    list1.append(chr(j))

for k in range(48,58):
    list1.append(chr(k))

ma = random.sample(list1,6)
print(ma)   #此时ma为列表
ma = ''.join(ma)  #将列表转化为字符串
print(ma)

print(list1)