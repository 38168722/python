#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/26 13:54
# @Author  : Aries
# @Site    : 
# @File    : oldboy.py
# @Software: PyCharm
from multiprocessing import Process,Queue
import time,random
def consumer(q):
    while True:
        str=q.get()
        if str is None:break
        print("消费者吃了%s个包子"%str)
        time.sleep(random.randint(1,3))


def producter(seq,q):
    for item in seq:
        q.put(item)
        print("生产者做了%s个包子"%item)

if __name__ == '__main__':
    q=Queue()
    producter(("包子%s"%i for i in range(10)),q)
    p1=Process(target=consumer,args=(q,))
    p1.start()
    q.put(None)
