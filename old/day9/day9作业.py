#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 16:34
# @Author  : Aries
# @Site    : 
# @File    : day9作业.py
# @Software: PyCharm

# 　　 1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
# l=['a','b',1,'a','a']
# print(set(l))

#
# 　　 2.在上题的基础上，保存列表原来的顺序
# l=['a','b',1,'a','a']
# l2=list(set(l))
# print(l2)
#
# 　　 3.去除文件中重复的行，肯定要保持文件内容的顺序不变
# 　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
#
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]

all=[]
for item in l:
    if item not in all:
        all.append(item)

print(all)


