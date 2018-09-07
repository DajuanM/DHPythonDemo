# lambda
stm = lambda x: 100 * x
num = stm(5)
print(num)
stm = lambda x,y,z: x + y + z
num = stm(1,2,3)
print(num)


# 函数名称就是一个变量
def funA():
    print("In funA")


funB = funA
funB()

def funB(n):
    return n * 2

def funC(n, f):
    return f(n) * 3
num = funC(3, funB)
print(num)

# map reduce filter
l = map(funB, [1, 2, 3])
for i in l:
    print(i)
# ??????
l = [i for i in l]
print(l)

from functools import reduce

def add(x, y):
    return x + y
num = reduce(add, [1, 2, 3, 4])
print(num)

def isEven(a):
    return a % 2 == 0
l = filter(isEven, [1, 2, 3, 4, 5, 6])
print([i for i in l])

# 排序
a = [5, 1, 6, 2, 8, 9]
al = sorted(a, reverse=True)
print([i for i in al])
a = [5, 1, -6, 2, 8, -9]
al = sorted(a, key=abs, reverse=False)
print([i for i in al])
# sorted案例

astr = ['dana', 'Danaa', 'wangxiaojing', 'jingjing', 'haha']

str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.lower)
print(str2)

# 闭包（closure）
# 闭包常见坑
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
# 出现的问题：
#
# 造成上述状况的原因是,返回函数引用了变量i， i并非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3，最终调用的时候，都返回的是 3*3
# 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
# 解决方案： 再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变
def count():
    def f(i):
        def g():
            return i * i
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 装饰器(Decrator)
import time

# 高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper
# 上面定义了装饰器，使用的时候需要用到@， 此符号是python的语法糖
@printTime
def hello():
    print("Hello world")
hello()


# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数

def hello3():
    print("我是手动执行的")


hello3()

hello3 = printTime(hello3)
hello3()

f = printTime(hello3)
f()

# 偏函数
t = int("12345")
print(t)
t = int("12345", base=8)
print(t)
# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字
def int16(x, base=16):
    return int(x, base)
print("------")
print(int16("12345"))

import functools
# 参数固定的函数，相当于一个由特定参数的函数体
# functools.partial的作用是，把一个函数某些函数固定，返回一个新函数
#实现上面int16的功能
int16 = functools.partial(int, base=16)
print(int16("12345"))

