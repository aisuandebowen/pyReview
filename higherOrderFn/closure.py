# 闭包 返回一个函数，此函数使用外部的变量


def getFnList():
    fnList = []
    for i in range(1, 4):

        def fn():
            return i * i

        fnList.append(fn)

    return fnList


fn1, fn2, fn3 = getFnList()
# i一直被引用 非立即执行
print(fn1(), fn2(), fn3())


def getFnList2():
    fnList = []

    def fn(i):
        def g():
            return i * i

        return g

    for i in range(1, 4):
        fnList.append(fn(i))

    return fnList


fn1, fn2, fn3 = getFnList2()
# i一直被引用 非立即执行
print(fn1(), fn2(), fn3())
