#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 9:19
# @Author  : Aries
# @Site    : 
# @File    : 线程池.py
# @Software: PyCharm
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import threading,os,time,random
def task(n):
    print("%s:%s is running"%(threading.current_thread().getName(),os.getpid()))
    time.sleep(2)
    return n**2

if __name__ == '__main__':
    p=ThreadPoolExecutor()
    l=[]
    start=time.time()
    for i in range(10):
        obj=p.submit(task,i)
        l.append(obj)
    p.shutdown()
    print("="*30)
    print([obj.result() for obj in l])
    print(time.time()-start)