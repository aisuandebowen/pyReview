def getSum(*args):

    def calc():
        sum = 0
        for num in args:
            sum += num
        return sum

    return calc


sum = getSum(1, 2, 3, 4, 5)
print(sum())
