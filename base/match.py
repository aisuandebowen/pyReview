# score = int(input("please input ur score:"))
score = 100

match score:
    case score if score > 90:
        print("NO.1")
    case 90 | 89 | 11:
        print("just so so")
    case _:
        print("I dont know")


# 匹配列表
args = ["A", "B", "C", "D"]

match args:
    case ["A", letter1, *letters]:
        print("啦啦啦：" + letter1 + " and " + ",".join(letters))
