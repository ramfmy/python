#判断字符串是否只由数字组成
'''
知识点：
1. unicodedata的使用
2. except使用
'''

#方法一
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
        print("aaa")
    #下面是检测数是否是汉字的数字
    #比如：汉字"一"通过unicodedata.numeric("一")
    #返回的就是1.0
    try:
        print("bbb")
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass
    return False

t = "'9'"
print(is_number(t))

#方法二
#这种方法检测不了unicode对象
print("方法二")
t = "q123"
print(t.isdigit())

#方法三
'''
isnumeric使用示例：
>>> "1".isnumeric()
True
>>> "一".isnumeric()
True
>>> "我".isnumeric() 
False
'''
#这种方法只针对unicode对象
t = "123"
print(t.isnumeric())