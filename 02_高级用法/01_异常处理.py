try:
    num = int(input("输入数字"))
    raise NameError
    rst = 100/num
    print("计算结果是：",rst)
# except:
#     print("出错啦！！！")
except ZeroDivisionError as e:
    print(e)
    exit()
except NameError as e:
    print("名字错误")
    exit()
except Exception as e:
    print("其他错误")