for i in range(1,10):
    for j in range(1,i+1):
        #通过指定end参数的值，可以取消在末尾输出回车符，实现不换行
        print("%d x %d = %d \t"%(j,i,i*j),end='')

    print()