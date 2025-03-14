# 字典

d = {"Adam": 96, "Douaa": 100}
print(d["Adam"])

for key in d:
    print(f"{key} got {d[key]}")

# 如果Key不在 返回后边儿的
print(d.get("Douaa", -1))

# set 不重复
s = {1, 1, 2, 3}
s.add(99)

s.remove(2)
print(s)

str = "123456"
str2 = str.replace("1", "A")
print(f"{str} and {str2}")
