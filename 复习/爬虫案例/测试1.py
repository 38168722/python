#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 18:44
# @Author  : Aries
# @Site    : 
# @File    : 测试1.py
# @Software: PyCharm
import urllib
from urllib.request import urlopen
import re
import time
def down_pic(picts):
    i = 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    for url in picts:
        with open(str(i) + '.jpg', 'wb') as f:
            req = urllib.request.Request(url=url, headers=headers)
            buf = urllib.request.urlopen(req).read()
            f.write(buf)
            print("%s.jpg"%i)
            i += 1
def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    s = urllib.request.urlopen(req).read()
    s = s.decode("gbk")
    hrefs = re.compile(r'src=\"(.*?)\"')
    link =re.findall(hrefs,s)
    links=[]
    for x in link:
        if x.startswith("http") and x.endswith(".jpg"):
            links.append(x)
        elif x.endswith(".jpg"):
            x = "http://www.xiaohuar.com " + x
            links.append(x)
    return links


s=get_url("http://www.xiaohuar.com/ ")
for x in s:
    print(x)
down_pic(s)
