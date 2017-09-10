#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 19:57
# @Author  : Aries
# @Site    : 
# @File    : 文件编码.py
# @Software: PyCharm
# f = open("test1",'wb')
# f.write("老男孩".encode("gbk"))

with open("test1",'wb') as write_f:
    write_f.write("老男孩".encode("gbk"))

with open("test1",'rb') as read_f:
    print(read_f.readline().decode("gbk"))