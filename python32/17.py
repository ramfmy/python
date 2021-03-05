#计算平方根
'''
知识点：
1. x ** y 幂 - 返回x的y次幂
2. %0.2f 小数点后取两位
'''
num = float(input("请输入一个数字："))
num_sqrt = num ** 0.5
print("%0.2f 的平方根为%0.2f"%(num, num_sqrt))