num = ["harden","lampard",3,4,5,6,3,8,9,0]

print(num.count(3))
print(num.index(3))
print(num.index("harden"))
print(num.index("lampard"))

for i in range(num.count(3)):
    ele_index = num.index(3)  #获取首次3出现的坐标
    num[ele_index] = "3a"

print(num)