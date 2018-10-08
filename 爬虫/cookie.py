# -*- coding: utf-8 -*-
from urllib import request
from http import cookiejar

#创建一个用于保存cookis的文件
file = "cookie.txt"
#声明一个MozillaCookieJar实例来保存cookie，之后写入文件
cookie = cookiejar.MozillaCookieJar(file)
#创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#构建opener
opener = request.build_opener(handler)
#
response = opener.open('http://www.baidu.com')
#保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)