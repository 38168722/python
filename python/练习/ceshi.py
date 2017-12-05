#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 8:17
# @Author  : Aries
# @Site    : 
# @File    : ceshi.py
# @Software: PyCharm

# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
# def eat():
#     print("eat food 1")
#     time.sleep(2)
#     print("eat food 2")
#
# def play():
#     print("play1")
#     time.sleep(1)
#     print("play2")
# g1=gevent.spawn(eat)
# g2=gevent.spawn(play)
# gevent.joinall([g1,g2])
# print("主")

def hello(**kwargs):
    print("kwargs是什么数据类型%s"%type(kwargs))
    print(kwargs.get("name"))
hello(name="egon")