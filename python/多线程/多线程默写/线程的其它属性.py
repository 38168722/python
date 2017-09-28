#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 10:03
# @Author  : Aries
# @Site    : 
# @File    : 线程的其它属性.py
# @Software: PyCharm
from threading import Thread,currentThread,activeCount
import os,time,threading
def talk():
    print("%s is running"%currentThread().getName())

if __name__ == '__main__':
    t=Thread(target=talk)
    t.start()
    print(threading.enumerate())
    time.sleep(3)
    print(t.is_alive())
    print("主",activeCount)