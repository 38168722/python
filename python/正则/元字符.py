#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 12:10
# @Author  : Aries
# @Site    : 
# @File    : 元字符.py
# @Software: PyCharm
import re
# ret = re.findall("-?\d+","121,-41,-65,87")
# ret = re.findall("\.com","www.baidu.com")
# print(ret)
# ret = re.findall("\w+","yuan123$888")
# print(ret)

# ret = re.findall(r"I\b","hello I am LIST")
# print(ret)
# ret = re.findall(r"c\\l","abc\le")
# print(ret)
# ret = re.findall("(yuan)+","yuannnyuanyuanlkdsa")
# print(ret)

# ret = re.findall(r"(李.{1,3}),","李杰,李刚,李占三,王二,李二棍子,")
# print(ret)

# ret = re.search(r"\d+","123fdsafds321#43")
# print(ret.group())

# ret = re.match("\d+","aa123fdsafds321#43")
# print(ret.group())

# ret=re.search(r"(?P<year>2[01]\d{2})-(?P<month>\d{1,2})","-blog-article-2004-12")
# print(ret.group("year"))
# print(ret.group("month"))

# ret =re.findall(r"a[bf]c","afciiabcabfc")
# print(ret)

# ret = re.findall("www\.(?:\w+)\.(?:com|cn)","www.oldboy.com;www.oldboy.cn;www.baidu.com;www.sina.com")
# ret = re.findall("c.d","abc\nd",re.S)
# print(ret)

# ret=re.findall("\d{0,8}","8789afdsads")
# print(ret)
# s="<div>yuan<img></div><a href=""></div>"
# ret = re.findall("<div>.*?</div>",s)
# print(ret)
s="hello123world123afdsaf2321fdsa21321"

ret=re.finditer("\d+",s)
for i in ret:
    print(i.group())