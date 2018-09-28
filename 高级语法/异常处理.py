# -*- coding: utf-8 -*-
class zero(Exception):#自定义异常继承父类异常
    pass
try:
    num = int(input("shuru:"))
    if num == 0:

        raise zero#自定义抛出异常

    rst = 100/num
    print("结果是：{0}".format(rst))

except ZeroDivisionError as e:#捕获ZeroDivisionError异常并实例化实例e
    print("shutucuowu")
    print(e)
    exit()#退出程序
except zero as e:
    print(e)
    print("bunengshuru0")
    exit()
except Exception as e:
    print(e)
    exit()