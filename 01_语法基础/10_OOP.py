# python可多继承
class Person():
    name = None
    age = 17
    __sex = None # private 成员
    _b = None # protect 成员
    def __init__(self): # 如果子类实现了init函数，则不再调用父类的init函数
        self.name = "Aiden"
        self.age = 24
    def eat(self):
        print("吃饭")

class Dog():
    num = None
    # 构造函数
    def __init__(self, num):
        self.num = num

    def func(self):
       print("调用函数")

class Student(Person, Dog): # 继承
    name = None
    age = 18

    def doHomework(self):
        print(self.name)
        print(self.age)
        print("做作业")

stu = Student()
stu.doHomework()

Student.doHomework(stu)
Student.doHomework(Student)
# Person 有name,age就不会报错
Student.doHomework(Person())

stu.eat()
stu.func()


# 多继承 菱形问题
# Mixin设计模式 采用多继承对类进行功能拓展
class A():
   def func(self):
       print("A func")
class B(A):
    def func(self):
        print("B func")
class C(A):
    def func(self):
        print("C func")
class D(B, C):
    pass

# MRO 保存继承顺序
print(D().func())

# issubclass(A, B)
# isinstance(a, A)
# hasattr(a, "name")
# getattr setattr delattr dir获取成员列表

class E():
    def __init__(self):
        self.name = "haha"
        self.age = 18

    # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("我被读取了")
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self, name):
        print("我被写入了，但是还可以左好多事情")
        self.name = "图灵学院：" + name

        # fdel模拟的是删除变量的时候进行的操作

    def fdel(self):
        pass

    # property的四个参数顺序是固定的
    # 第一个参数代表读取的时候需要调用的函数
    # 第二个参数代表写入的时候需要调用的函数
    # 第三个是删除
    name2 = property(fget, fset, fdel, "这是一个property的例子")


e = E()
print(e.name)
e.name2 = "qwe"
print(e.name2)

# 利用type造一个类


# 先定义类应该具有的成员函数
def say(self):
    print("Saying.....")


def talk(self):
    print("Talking .....")


# 用type来创建一个类
F = type("AName", (object,), {"class_say": say, "class_talk": talk})

# 然后可以像正常访问一样使用类
a = F()

a.class_say()
a.class_talk()


# 元类演示

# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务处理
        print("哈哈，我是元类呀")
        attrs['id'] = '000000'
        attrs['addr'] = "北京海淀区公主坟西翠路12号"
        return type.__new__(cls, name, bases, attrs)


# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=TulingMetaClass):
    pass


t = Teacher()

t.id


# 自己组装一个类

class H():
    pass


def say(self):
    print("Saying... ...")


class I():
    def say(self):
        print("Saying......")


say(9)
H.say = say

a = H()
a.say()

b = I()
b.say()

from types import MethodType


class G():
    pass


def say(self):
    print("Saying... ...")


a = G()
a.say = MethodType(say, G)
a.say()


import abc
# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(self):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("Sleeping.......")