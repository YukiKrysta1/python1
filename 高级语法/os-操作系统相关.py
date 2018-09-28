# -*- coding: utf-8 -*-
#os:操作系统目录相关
#os.path:系统路径相关操作
#shutil:高级文件操作，目录树的操作，文件赋值，删除，移动
import os

mydir = os.getcwd()#获取当前工作目录
print(mydir)
#os.chdir():切换当前目录
os.listdir()#获取一个目录中所有子目录和文件的名称列表
#makedirs():创建一个递归路径
#os.system():运行系统shell命令
#os.getenv():获取指定的系统环境变量
#os.putenv():
#os.path.abspath():将路径转化为绝对路径
#os.path.basename():获取路径中的文件名称
#os.path.join():将多个路径拼成一个路径
#os.path.split():将路径切割为文件夹和当前文件（元祖形式）
#os.path.exists():检测文件或目录是否存在
#归档：
#shutil.make_archive("归档之后的目录和文件名",""后缀,"需要归档的文件夹")：后缀：zip,tar,gztar
#shutil.unpack_archive()
#压缩包
#import zipfile
#zf = zipfile.ZipFile(路径):创建一个zip对象表示一个zip文件
#rst = zf.getinfo(路径):获取zip文档内指定文件的信息
#namelist():获取zip文件所有文件名称
#rst = zf.exteactall(路径)：解压
#

