#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/26 11:06
# @Author  : Aries
# @Site    : 
# @File    : 生产者消费者joinQueue方法使用.py
# @Software: PyCharm
from multiprocessing import Process,JoinableQueue
import time,random
def consumer(q):
    while True:
        res=q.get()
        print("消费者拿到了%s"%res)
        q.task_done()

def producer(seq,q):
    for item in seq:
        q.put(item)
        print("生产者做好了%s"%item)
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    seq=("包子%s"%i for i in range(10))
    p=Process(target=consumer,args=(q,))
    p.daemon=True
    p.start()
    producer(seq,q)
    print("主进程")