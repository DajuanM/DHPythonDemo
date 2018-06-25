# while
a = 1
while a < 10:
    print(a)
    a += 1
else:
    print("循环结束")

# 函数
# - 普通参数
# - 默认参数
# - 关键字参数
# - 收集参数
def func(name):
    return "姓名是：{}".format(name)
str = func("aiden")
print(str)

def reg(name, age, gender = "male"):
    if gender == "male":
        print("{0} is {1}, and he is good".format(name, age))
    else:
        print("{0} is {1}, and she is good".format(name, age))
reg("aiden", 24)
reg("lucy", 18, "female")

def fun1(name = "", age = 0):
    print("{0} is {1}".format(name, age))
print(fun1(name="aiden", age=18))

def stu(name, age, *agrs, hobby = "没有", **kwargs):
    print("------------")
    print(name)
    print(age)
    for i in agrs:
        print(i)
    print(hobby)
    for k, v in kwargs.items():
        print(k, ":", v)

name = "liuying"
age = 19
stu(name, age)

stu(name, age, hobby="游泳")

stu(name, age, "王晓静", "刘石头", hobby="游泳", hobby2="烹饪", hobby3="跟不同女生聊天")

print(help(stu))
print(stu.__doc__)

