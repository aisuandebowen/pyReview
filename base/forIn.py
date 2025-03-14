names = ["Peter", "Adam", "Douaa"]

for name in names:
    print(name)


sum = 0
for num in [1, 2, 3, 4, 5, 6]:
    sum += num

arr = range(5)
print(list(arr))


while sum > 10:
    sum -= 1
    if sum == 14:
        continue
    print(sum)
    if sum == 11:
        print("I'll break")
        break
