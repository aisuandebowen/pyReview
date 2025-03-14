# 函数本身也可以赋值给变量，即：变量可以指向函数。
from functools import reduce

print(abs(-10))

f = abs
print(f(10))


def calc(x, y, fn):
    return fn(x) + fn(y)


res = calc(-1, 3, abs)
print(res)


# map
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def calc(x):
    return x * x


list1 = map(calc, [2, 4, 6, 8, 10])
print(list(list1))


# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x, y):
    return x + y + 10


res = reduce(fn, [1, 2, 3, 4, 5, 6])
print(res)

codeBook = {"1": "你", "2": "我", "3": "他", "4": "吃", "5": "饭", "6": "屎"}


def myDecode(codes):
    def getCode(key):
        return codeBook[key]

    def fn(x, y):
        return x + y

    return reduce(fn, map(getCode, codes))


mycodes = myDecode("146")
print(list(mycodes))
