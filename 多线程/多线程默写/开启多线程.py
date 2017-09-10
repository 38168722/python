#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 15:14
# @Author  : Aries
# @Site    : 
# @File    : 开启多线程.py
# @Software: PyCharm
from threading import Thread
from multiprocessing import Process
import os
def work():
    global n
    n=0

if __name__ == '__main__':
    n=1
    t=Process(target=work)
    t.start()
    t.join()
    print("主",n)