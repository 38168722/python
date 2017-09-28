#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 12:17
# @Author  : Aries
# @Site    : 
# @File    : 生产者消费者模型.py
# @Software: PyCharm
from multiprocessing import Process,JoinableQueue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print("\033[45m%s 吃了 %s\033[0m"%(os.getpid(),res))
        q.task_done()
def product_baozi(q):
    for i in range(5):
        time.sleep(2)
        res="包子%s"%i
        q.put(res)
        print("\033[44m%s制造了%s\033[0m"%(os.getpid(),res))
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    p1=Process(target=product_baozi,args=(q,))
    p4=Process(target=consumer,args=(q,))
    p4.daemon=True
    p1.start()
    p4.start()
    p1.join()
    print("主")