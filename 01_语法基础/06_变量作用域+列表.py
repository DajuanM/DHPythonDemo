# 变量作用域
# 变量由作用范围限制
# 分类：按照作用域分类
# 全局(global): 在函数外部定义
# 局部（local)：在函数内部定义
# 变量的作用范围：
# 全局变量：在整个全局范围都有效
# 全局变量在局部可以使用（即函数内部可以方位函数外部定义的变量）
# 局部变量在局部范围可以使用
# 局部变量在全局范围无法使用
# LEGB原则
# L（Local）局部作用域
# E（Enclosing function locale）外部嵌套函数作用域
# G（Global module）函数定义所在模块作用域
# B（Buildin）： python内置魔抗的作用域


# global
a = 1
def func():
   global b
   b = 2
func()
print(b)

def func1():
    c = 3
    print("locals {0}".format(locals()))
    print("global {0}".format(globals()))
func1()

# eval()函数
# 把一个字符串当成一个表达式来执行， 返回表达式执行后的结果
print(eval("a+b"))

# exec()函数
# 跟eval功能类似， 但是，不返回结果
x = 100
y = 200
# 执行x+y
# z = x + y
z1 = x + y
# 1, 注意字符串中引号的写法
# 2. 比对exec执行结果和代码执行结果
z2 = exec("print('x+y:', x+y)")

print(z1)
print(z2)

# id()函数
# 内置函数id，负责显示一个变量或者数据的唯一确定编号
print(id(a))
# 分片
l = [1,2,3,4,5,6]
ll = l[1:4]
print(l[1:6:1]) # 起点 : 终点 : 每次＋几
print(l[-4:-2])
print(l[-2:-4:-1])
