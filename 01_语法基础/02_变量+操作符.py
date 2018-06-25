s = "let's go"
print(s)

ss = 'let\'s go'
print(ss)

sss = "c:\\user"
print(sss)

s1 = "i love \t\n you"
print(s1)

# 格式化
s2 = "i love %s"
print(s2 % "123")

s3 = "i am %s, i am %d years old"
print(s3%("wei", 18))

s4 = "i am {}".format("wei")
print(s4)

s = "i am {1} years old, i love {0} and i am {1} years old".format("wei", 18)
print(s)


# 算术运算符
# python2.0 取整 python3.0 数学运算
a = 9 / 4
print(a)
# 取余
a = 9 % 4
print(a)
# 取商
a = 9 // 4
print(a)
# 幂运算
a = 9**4
print(a)
b = a == 80
print(b)

# 赋值运算符
# += -= *= /= **=

# 逻辑运算符
# and 与 or 或 not 非
a = True
b = False
c = True
print(a and b or c)
c = b or (a==9) and c
print(c)

# 成员运算符
l = [1,2,3,4,5]
a = 7
b = a in l
c = a not in l
print(b)
print(c)

# 身份运算符
a = 7
b = 7
c = a is b
print(c)
c = a is not b
print(c)
a = "i am aiden"
b = "i am aiden"
c = a is b
print(c)