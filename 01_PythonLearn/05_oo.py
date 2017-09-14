class Person :
    def __init__(self, name):
        self.name = name

    def sayHello (self):
        print("{0} say hello!".format(self.name))

p = Person("aiden")
p.sayHello()
print(p.name)
# 继承
class Student:
    def __init__(self, name):
        Person.__init__(self, name)
