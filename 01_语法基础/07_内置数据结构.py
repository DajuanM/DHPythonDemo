# 汉诺塔
def hano(n, a, b, c):
    if n == 1:
        print("A --> C")
        return None
    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None

    # 先把n-1个盘子从a挪到b
    hano(n-1, a, c, b)
    # 最大的盘子从a挪到c
    print("A --> C")
    # 再把n-1个盘子从b挪到c
    hano(n-1, b, a, c)

hano(3, "A", "B", "C")

# 列表
a = [1, 2, 3]
b = [4, 5, 6]
c = ["a", "b", "c"]
print(len(a))
print(a + b + c)
print(a * 2)
print(2 in a)
# 删除
del  a[0]
print(a)

# 双层列表循环

#a 为嵌套列表，或者叫双层列表
a = [["one", 1], ["two", 2], ["three", 3]]
# 数量必须一致
for k,v in a:
    print(k, "--", v)

d = [i*10 for i in b]
print(d)
d = [i for i in b if i % 2 == 0]
print(d)
e = [m+n for m in b for n in d]
print(e)
# 最大值
print(max(e))
print(max(["qwe", "q", "qqwqqwqww"]))

# list
s = "i love you"
print(list(s))
print(list(range(1, 10)))

