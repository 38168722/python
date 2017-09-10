#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 11:49
# @Author  : Aries
# @Site    : 
# @File    : event协程.py
# @Software: PyCharm
from gevent import monkey;monkey.patch_all()
import gevent
import time
def eat(name):
    print("%s eat 1"%name)
    time.sleep(2)
    print("%s eat 2"%name)
    return "eat"

def play(name):
    print("%s play 1"%name)
    time.sleep(1)
    print("%s play 2"%name)
    return "play"

start=time.time()
g1=gevent.spawn(eat,"egon")
g2=gevent.spawn(play,"egon")
gevent.joinall([g1,g2])
print("主",(time.time()-start))
print(g1.value)
print(g2.value)