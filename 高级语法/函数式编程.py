# -*- coding: utf-8 -*-
#lamba表达式
#stm = lambda x: 100 * x
#stm(10)
from functools import reduce

#map
l = [i for  i in range(11)]
def numTen(n):
    return n * 10
l2 = map(numTen,l)
print(l2)

#reduce 需要导入functools包
def Add(x,y):
    return x + y
rst = reduce(Add,l)
print(rst)

#filter
def isEven(a):
    return a % 2 == 0
rst = filter(isEven,l)
print(rst)

#排序
rst = sorted(l, key=abs, reverse=True)
print(rst)

#装饰器
import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time:",time.ctime())
        return f(*args, **kwargs)
    return wrapper

#偏函数
import functools
int = functools.partial(int,base = 16)#把一个函数的某些参数固定 返回一个新函数

#nametuple:
import collections
c = collections.namedtuple("c",['x','y','r'])
C = c(100,150,50)
print(C)

#dequeue比较方便的解决了频繁删除插入带来的效率问题
from collections import deque

#defaultdict
from collections import defaultdict

