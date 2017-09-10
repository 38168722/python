#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 16:55
# @Author  : Aries
# @Site    : 
# @File    : 测试.py
# @Software: PyCharm

# def init(func):
#     def inner(*args,**kwargs):
#         g=func(*args,**kwargs)
#         next(g)
#         return g
#     return inner
#
# @init
# def averager():
#     total=0.0
#     count=0
#     average=None
#     while True:
#         term=yield average
#         total+=term
#         count+=1
#         average=total/count
# g_avg=averager()
# print(g_avg.send(10))
#
# from collections import Iterable
# from collections import Iterator
#
# map_o = map(abs,[1,2,3,4])
# print(list(map_o))
# print(isinstance(map_o,Iterable))
# res = filter(lambda x:x>10,[5,8,11,9,15])
# for i in res:
#     print(i)
# test = lambda t1,t2:[{i:j} for i,j in zip(t1,t2)]
# import math
# print(list(filter(lambda x:math.sqrt(x)%1==0,range(1,101))))
# from collections.Iterator
# map1=map(abs,[1,-2,3,-4])
# print(isinstance(map1,))
