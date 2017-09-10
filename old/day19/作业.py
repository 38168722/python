#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 16:34
# @Author  : Aries
# @Site    : 
# @File    : 作业.py
# @Software: PyCharm
# import time
# def timer(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         re=func(*args,**kwargs)
#         print(time.time()-start)
#         return re
#     return inner
# @timer
# def func1(a,b):
#     print("in func1")
#
# def func2(a):
#     print("in func2 and get a:%s"%a)
#     return 'func2 over'
#
# func1('aaaaa','bbbbb')
# print(func2('aaaaaa'))
# import time
# def timer(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         re=func(*args,**kwargs)
#         print(time.time()-start)
#         return re
#     return inner
#
# def func2(a):
#     print("in func2 and get a:%s"%a)
#     return 'func2 over'
#
# func2('aaaaaaa')
# print(func2('aaaaa'))
#
# def outer(flag):
#     def timer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print("执行函数之前要做的")
#             re = func(*args,**kwargs)
#             if flag:
#                 print("执行函数之后要做的")
#             return re
#         return inner
#     return timer
#
# @outer(False)
# def func():
#     print(1111)
#
# func()
#
# f = open('tmp_file','w')
# print(123,456,sep=',',file=f,flush=True)
import time
import sys
# for i in range(0,101,2):
#     time.sleep(0.1)
#      char_num = i//2      #打印多少个#
#      per_str = '%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
#      print(per_str,end='', file=sys.stdout, flush=True)
#
# hello world

def averager():
    total = 0.0
    count=0
    average=None
    while True:
        term=yield average
        total+=term
        count+=1
        average=total/count

g_avg = averager()
next(g_avg)
