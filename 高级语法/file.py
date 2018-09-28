# -*- coding: utf-8 -*-
import time
#open函数：打开文件

# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1",'r') as f:
#    strline = f.readline()#按行读取
#    while strline:
#        print(strline)
#         strline = f.readline()

# list读取
# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1",'r') as  f:
#     l = list(f)
#     for line in l:
#         print(line)

# read()读取
# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1", 'r') as f:
#     strChar = f.read(1)
#     while strChar:
#         print(strChar, end=" ")
#         strChar = f.read(1)
#     print(strChar)

# seek
# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1",'r') as f:
#     f.seek(4,0)
#     strChar = f.read()
#     print(strChar)

# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1", 'r') as f:
#     strChar = f.read(3)
#     while strChar:
#         print(strChar)
#         time.sleep(1)
#         strChar= f.read(3)

#tell():用来显示文件读写指针当前位置


#write(str):把字符串写入文件  , writelines(str)写入很多行，可以是list形式
# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1", 'a') as f:
#     f.write("123321")

#序列化：
#pickle.dump:序列化
#pickle.load:反序列化

# import pickle
# age = 18
# with open(r"C:\Users\Administrator\Desktop\新建文件夹\txt1", 'rb') as f:
#     print(pickle.load(f))


#shelve 类似字典kv对保存数据  shelve自动创建的不仅仅是一个.db文件，还包括其他格式文件
import shelve




