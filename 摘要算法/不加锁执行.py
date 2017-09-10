#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 14:40
# @Author  : Aries
# @Site    : 
# @File    : 不加锁执行.py
# @Software: PyCharm
from threading import current_thread,Thread,Lock
import os,time
def task():
    global n
    print("%s is running"%current_thread().getName())
    temp=n
    time.sleep(0.5)
    n=temp-1

if __name__ == '__main__':
    n=100
    lock=Lock()
    threads=[]
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    stop_time=time.time()
    print("主:%s n:%s"%(stop_time-start_time,n))