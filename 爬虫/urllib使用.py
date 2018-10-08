# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({"hello":"word"}), encoding="utf-8")
response = urllib.request.urlopen('http://www.httpbin.org/post', data = data)
print(response.read())