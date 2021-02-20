def power(x,n):
    s = 1;
    while n > 0:
        n = n - 1
        s = s * x
    return s


if __name__ == '__main__':
    print(power(3,4))