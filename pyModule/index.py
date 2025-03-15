# 模块 module

# 相同名字的函数和变量完全可以分别存在不同的模块中

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。

import sys
import caculate

res = caculate.calc(1,2)

print(caculate.__doc__)

print(sys.argv,res)