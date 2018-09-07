# tuple 元祖 不能修改！！！
# list的特性除了修改其他都有

t = (1, 2, 3)
t = 1, 2, 3
print(type(t))
print(t)
a = [1, 2, 3]
t = tuple(a)
print(t)

# 利用元祖交换值
a = 1
b = 2
a, b = b, a
print(a, "-", b)

# set 集合
# 集合的定义
s = set()
print(type(s))
print(s)

# 此时，大括号内一定要有值，否则定义出的是一个dict
s = {1,2,3,4,5,6,7}
print(s)
# 如果只是用大括号定义，则定义的是一个dict类型
d = {}
print(type(d))
print(d)
# 集合的特征
#
# 集合内数据无序，即无法使用索引和分片
# 集合内部数据元素具有唯一性，可以用来排除重复数据
# 集合内的数据，str, int, float, tuple,冰冻集合等，即内部只能放置可哈希数据

# set:生成一个集合
l = [1,2,3,4,3,23,1,2,3,4]
s = set(l)
print(s)

s = {1}
s.add(334)
print(s)

# copy:拷贝
# remove:移除制定的值，直接改变原有值，如果要删除的值不存在，报错
# discard:移除集合中指定的值，跟ｒｅｍｖｏｅ一样，但是入股要删除的话，不报错
s = {23,3,4,5,1,2,3}
s.remove(4)
print(s)
s.discard(1)
print(s)

print("*" * 20)
s.discard(1100)
print(s)

# s.remove(1100) 不存在报错
print(s)


# 集合函数
# intersection: 交集
# difference:差集
# union: 并集
# issubset: 检查一个集合是否为另一个子集
# issuperset: 检查一个集合是否为另一个超集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)

# frozen set:冰冻集合
#
# 并冻和就是不可以进行任何修改的集合
# frozenset是一种特殊集合
s = frozenset()
print(type(s))
print(s)


# dict 字典
# 字典的创建
# 创建空字典1
d = {}
print(d)

# 创建空字典2
d = dict()
print(d)

# 创建有值的字典， 每一组数据用冒号隔开， 每一对键值对用逗号隔开
d = {"one":1, "two":2, "three":3}
print(d)

# 用dict创建有内容字典1
d = dict({"one":1, "two":2, "three":3})
print(d)

# 用dict创建有内容字典2
# 利用关键字参数
d = dict(one=1, two=2, three=3)
print(d)


#
d = dict([("one",1), ("two",2), ("three",3)])
print(d)

# 成员检测， in， not in
# 成员检测检测的是key内容
d = {"one": 1, "two": 2, "three": 3}

# if 2 in d:
#     print("value")

if "two" in d:
    print("key")

# if ("two", 2) in d:
#     print("kv")

# 遍历字典
# 便利在python2 和 3 中区别比较大，代码不通用
# 按key来使用for循环
d = {"one": 1, "two": 2, "three": 3}
# 使用for循环，直接按key值访问
for k in d:
    print(k, d[k])

# 上述代码可以改写成如下
for k in d.keys():
    print(k, d[k])

# 只访问字典的值
for v in d.values():
    print(v)

# 注意以下特殊用法
for k, v in d.items():
    print(k, '--', v)

d = {"one":1, "two":2, "three":3}
print(str(d))
# 常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)


# 加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v % 2 == 0}
print(dd)

# get: 根据制定键返回相应的值， 好处是，可以设置默认值

d = {"one":1, "two":2, "three":3}
print(d.get("on333"))

# get默认值是None，可以设置
print(d.get("one", 100))
print(d.get("one333", 100))

#体会以下代码跟上面代码的区别
# print(d['on333'])

# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ["eins", "zwei", "drei"]
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
d = dict.fromkeys(l, "hahahahahah")
print(d)
