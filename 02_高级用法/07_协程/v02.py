
def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)

    d = yield a + b + c
    print('-> recived', a, b, c, d)

# runc
sc = simple_coroutine(5)
print("=====")
aa = next(sc)
print(aa)
bb = sc.send(6) # 5, 6
print(bb)
cc = sc.send(7) # 5, 6, 7
print(cc)

