# -*- coding: utf-8 -*-
import re
import requests

html = requests.get('http://book.douban.com').text
# with open(r'C:\Users\Administrator\Desktop\新建文件夹\html.txt','wb') as f:
#     f.write(html.encode())


pa1 = re.compile('<div class="cover">.*?<a href="(.*?)" title="(.*?)">.*?</div>', re.S)

results = re.findall(pa1, html)
for rs in results:
    url, name = rs
    print(url, name)
# for result in results:
#     url, name = result
#     print(url, name)

