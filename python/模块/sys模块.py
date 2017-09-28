#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 8:00
# @Author  : Aries
# @Site    : 
# @File    : sys模块.py
# @Software: PyCharm
# import sys
# while True:
#     name = input(">>")
#     password = input(">>")
#     if name=="egon" and password=="123":
#         sys.exit()
import os
import sys

#
# ret = sys.argv
# if "-u" in ret and "-p" in ret:
#     username=ret[ret.index("-u")+1]
#     password=ret[ret.index("-p")+1]
#     if username=="egon" and password=="123":
#         print("login ok")
#     else:
#         print("login is failed")
sys.path.append(r"C:\Users\SKY\PycharmProjects\摘要算法")
import osceshi
import re
osceshi.func()
print(sys.path)
print(re.findall("hello","www.google"))