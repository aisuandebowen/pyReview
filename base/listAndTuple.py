# list

classmates = [1,3,2,'123']

print(classmates[-1])

classmates.append(['A','SS'])

classmates.insert(1,'Piii')
classmates.pop()
print(classmates)

# tuple
# 初始化后不可修改

myFoods = (1,2,['111','222'])
onlyOne = (2,) # 元组里只有一个元素

myFoods[2][0] = '我嘞个扫福'
print(myFoods)