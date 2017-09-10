#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 16:42
# @Author  : Aries
# @Site    : 
# @File    : 闭包函数.py
# @Software: PyCharm
import time


def timer(func):
    def inner(*args,**kwargs):
        start=time.time()
        re=func(*args,**kwargs)
        print(time.time()-start)
        return re
    return inner

def func1(a,b):
    print('in func1')

def func2(a):
    print('in func2 and get a:%s'%(a))
    return 'fun2 over'

func1('aaaaaa','bbbbbbb')
print(func2('aaaaaaaaaaa'))