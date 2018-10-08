# -*- coding: utf-8 -*-
from  urllib import request
from  urllib import error
import socket

try:
    response = request.urlopen('http://www.yk.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully")