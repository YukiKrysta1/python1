# -*- coding: utf-8 -*-
import urllib.request

prox_handler = urllib.request.ProxyHandler({
    #代理地址（字典）
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(prox_handler)
response = opener.open('http://www.baidu.com')
print(response.read())