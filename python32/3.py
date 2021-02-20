#给定一个数列，例如[1,2,3,4,5]，计算1*1+2*2+3*3+4*4+5*5的值
def cal_1(num):
    sum = 0
    for i in num:
        sum = sum + i * i
    return sum

#给定一个数列，例如[1,2,3,4,5]，计算1^1+2^2+3^3+4^4+5^5的值
#约定：0^0为1
def cal_2(num):
    sum = 0
    for i in num:
        sum = sum + cal_3(i)
    return sum

def cal_3(num):
    sum = 1;
    n = num;
    while n > 0:
        n = n -1
        sum = sum * num
    return sum

if __name__ == '__main__':
    test_num = [1,2,3,4,5]
    print(cal_1(test_num))
    test_num2 = [1,2,3]
    print(cal_2(test_num2))
    test_num3 = [0,1,2]
    print(cal_2(test_num3))