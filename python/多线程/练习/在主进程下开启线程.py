#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 15:56
# @Author  : Aries
# @Site    : 
# @File    : 在主进程下开启线程.py
# @Software: PyCharm
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(5)
    print("end123")

def bar():
    print(456)
    time.sleep(2)
    print("end456")

t1=Thread(target=foo)
t2=Thread(target=bar)

t1.daemon=True
t1.start()
t2.start()
print("main.........")