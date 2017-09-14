import time

print("Hello world")
i = 5
print(i)
i = 6
print(i)

str = "hello world"
print(str[2:7])

arr = ["run", 1, "qwe", 4]
print(arr)

arr1 = arr
arr1[0] = 2
print("------------")
print(arr)
print(arr1)

dict = {"1":1,"2":2}
dict1 = dict
dict["1"] = 3
print(dict)
print(dict1)

s = arr[0]
if (s in arr):
    print("s在arr中")
else:
    print("s不在arr中")

a = 1
b = 1
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
if (a is b):
    print("a跟b是同一对象")
else:
    print("a跟b不是同一对象")

if (a == b):
    print("a跟b是同一对象")
else:
    print("a跟b不是同一对象")

# while循环
numbers = [1,2,3,4,5,6,7,8,9,10]
del numbers[9]
even = []
odd = []
while len(numbers) > 0:
    num = numbers.pop()
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

for i in range(1, 5):
    print(i)

localtime = time.localtime(time.time())
print("本地时间为：", localtime)
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

# 函数
def func ():
    print("调用了func函数")
    return

func()

# 类
class Person:
    age = 0
    def __init__(self, age):
        self.age = age
    def printAge(self):
        print "age: %d" % self.age

class child(Person):
    def printAge(self):
        print "child age: %d" % self.age