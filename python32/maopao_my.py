list = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]

def sortport(lis):      #列表传入不需要指定类型
    print(len(lis))
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis;         #返回值也不需要定义

if __name__ == '__main__':
    newList = sortport(list)
    print(newList)