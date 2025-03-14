import math

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 在函数内部的任何位置定义的变量，在函数体的其他部分都可以被访问和使用，只要该变量在使用之前已经被定义。
def myAbs(x):
    if isinstance(x, (int, float)) and x < 0:
        res = abs(x)
    else:
        res = -1
    res = math.sin(res)
    return res, 666


# 空函数
def nop():
    pass


a = -99
print(myAbs(a))


# 默认参数 默认参数必须指向不变对象！！！否则将一直存储
def caculate(x, y=99, pp=[123]):
    return x + y


def test(L=None):
    if L is None:
        L = []
    L.append("Greatest")
    return L


# 可变参数
def calc(*nums):
    sum = 0
    for num in nums:
        if isinstance(num, (int, float)):
            sum += num
    return sum


# 关键字参数
def person(**kw):
    if "name" in kw:
        print(kw)


extra = {"name": "Adam", "age": "30"}
person(**extra)
print(test())
print(calc(1, 2, 3, 4, 5, 7))
print(calc(*[1, 2, 3]))
print(caculate(100, 77))
