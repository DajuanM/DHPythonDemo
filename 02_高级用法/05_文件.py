# open函数
# - mode: 表示以什么方式打开文件
# - r: 只读
# - w: 只写， 没有自动创建
# - x: 创建方式打开，如果文件已存在，报错
# - a: append写入，以追加的方式对文件进行写入
# - b: binary写入， 以二进制方式写入
# - t: 文本方式打开
# - +：可读可写

# f: 称为文件句柄
# r: 表示文件名不需要转义
# f = open(r"test01.txt", "w")
# f.close()

# with语句
# with是一种成为上下文管理协议的技术
# 自动判断文件的作用域，自动关闭不再使用的打开的文件句柄
with open(r"test01.txt", "r") as f:
    # strline = f.readline()
    # while strline:
    #     print(strline)
    #     strline = f.readline()
    l = list(f)
    print(l)

# read
with open(r"test01.txt", "r") as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)

# seek(offset, from)
# from: 0: 从文件头开始读取 1: 从当前位置读取 2: 从文件末开始读取
with open(r"test01.txt", "r") as f:
    f.seek(6, 0 ) # 一个汉字3个字符
    strChar = f.read()
    print(strChar)
print('---------------')
import time
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        strChar = f.read(3)

# tell函数 光标的位置
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()

# write
# with open(r"test01.txt", "a") as f:
#     f.write("生活不是眼前的苟且，\n还有远方的苟且")
# with open(r'test01.txt', 'a') as f:
#     # 注意字符串内含有换行符
#     f.writelines("生活不仅有眼前的苟且")
#     f.writelines("还有远方的枸杞")
# l = ["I", "love", "wangxiaojing"]
#
# # a代表追加方式打开
# with open(r'test01.txt', 'w') as f:
#     # 注意字符串内含有换行符
#     f.writelines(l)

# 持久化-序列化
import pickle

age = 18
with open(r"test02.txt", "wb") as f:
    pickle.dump(age, f)

with open(r"test02.txt", "rb") as f:
    a = pickle.load(f)
    print(a)

a = [19, "wei", "I'm good!"]
with open(r"test02.txt", "wb") as f:
    pickle.dump(a, f)

with open(r"test02.txt", "rb") as f:
    a = pickle.load(f)
    print(a)

# shelve
print("---------------")
import shelve

shv = shelve.open(r"shv.db")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()

# 不支持多个应用写入 使用flag
shv = shelve.open(r"shv.db", flag="r")
try:
    print(shv["one"])
    print(shv["two"])
    print(shv["three"])
except Exception as e:
    print("报错了")
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()
print("+++++++++")
# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
print("+++++++++")
# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

print("++++++++")
# shelve 使用with管理上下文环境

with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 1000

with shelve.open(r'shv.db') as shv:
    print(shv['one'])

