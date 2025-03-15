# 计算
def calc(x,y):
    res = f'{_getName()} has {x+y} dollars'
    return res

def _getName():
    return 'Adam'

if __name__ == '__main__':
    res = calc(1,1)
    print(res)