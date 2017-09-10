#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 16:13
# @Author  : Aries
# @Site    : 
# @File    : day8默写.py
# @Software: PyCharm

def register(name,age):
    pass

def wrapper(*args,**kwargs):
    print(type(args))
    register(*args,**kwargs)

x=1
def f1():
    x=1000
    def f2():
        def f3():
            print("内部",x)
        f3()
    f2()
f1()
print(x)
