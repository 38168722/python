#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 22:33
# @Author  : Aries
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from urllib.request import urlopen
def index(url):
    def inner():
        return urlopen(url).read()
    return inner
abc=index("http://www.baidu.com")
print(abc.__closure__[0])
