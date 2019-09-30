# 传值跟传址
def a(n):
    n[2] = 300
    print(n)
    return None

def b(n):
    n += 100
    print(n)
    return None


an = [1,2,3,4,5,6]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)

# 关于列表函数
a = [1, 2, 3, 4, 5]
print(a)
a.append(6)
print(a)
a.insert(2, 7)
print(a)
print(a.pop())
print(a.remove(1))
print(a.remove(7))
print(a.reverse())
b = [10, 11, 12]
print(a.extend(b))
print(a)
print(a.count(2))


c = a.copy()
# 深拷贝跟浅拷贝的区别
# 出现下列问题的原因是，copy‘函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1,2,3, [10, 20, 30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)


