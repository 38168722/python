#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 11:41
# @Author  : Aries
# @Site    : 
# @File    : 造包子.py
# @Software: PyCharm
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:
            break
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃了%s\033[0m'%(os.getpid(),res))

def producer(q):
    for i in range(5):
        time.sleep(2)
        res="包子%s"%i
        q.put(res)
        print('\033[44m%s 制造了 %s\033[0m' %(os.getpid(),res))
    q.put(None)

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=producer,args=(q,))
    p2=Process(target=consumer,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主")