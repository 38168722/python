#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 18:42
# @Author  : Aries
# @Site    : 
# @File    : 其它作业.py
# @Software: PyCharm
# 一、带参数的装饰器编写

# flag=True
# def outter(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print("之前要做的事")
#             ret=func(*args,**kwargs)
#             if flag:
#                 print("之后要做的事")
#             return ret
#         return inner
#     return wrapper
#
# @outter(flag)
# def ceshi():
#     print("第一次测试")
#
# ceshi()
#
# 二、函数、装饰器博客整理
#
# http://www.cnblogs.com/caoxing2017/articles/7259044.html

# input_str = input("输入查询语句==>").strip()
# element = [x.strip() for x in
#            (input_str[input_str.index("select") + 6:input_str.index("where")]).strip().split(",")]
# a = input_str[input_str.index("where") + 5:].strip()
# print(a)