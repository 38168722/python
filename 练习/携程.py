#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 11:22
# @Author  : Aries
# @Site    : 
# @File    : 携程.py
# @Software: PyCharm

from greenlet import greenlet
import time
def eat(name):
    print("%s eat 1"%name)
    time.sleep(10)
    g2.switch("egon")
    print("%s eat 2"%name)
    g2.switch()

def pay(name):
    print("%s play 1"%name)
    g1.switch()
    print("%s play 2"%name)
g1=greenlet(eat)
g2=greenlet(pay)
g1.switch("egon")
