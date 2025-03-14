# filter
def fn(num):
    return num > 10


res = filter(fn, [1, 5, 100, 23, 5, 15])
print(list(res))


# sorted
res2 = sorted(["Adam", "Pa", "Sam"])
print(res2)
