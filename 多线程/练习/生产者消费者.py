#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 15:11
# @Author  : Aries
# @Site    : 
# @File    : 生产者消费者.py
# @Software: PyCharm
from multiprocessing import Process,JoinableQueue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print("%s吃%s"%(os.getpid(),res))
        q.task_done()

def producer(name,q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res="%s%s"%(name,i)
        q.put(res)
        print("%s生产了%s"%(os.getpid(),res))
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    p1=Process(target=producer,args=("包子",q))
    p2=Process(target=producer,args=("骨头",q))
    p3=Process(target=producer,args=("泔水",q))

    #消费者们：即吃货们
    c1=Process(target=consumer,args=(q,))
    c2=Process(target=consumer,args=(q,))
    c1.daemon=True
    c2.daemon=True

    p_l=[p1,p2,p3,c1,c2]
    for p in p_l:
        p.start()
    p1.join()
    p2.join()
    p3.join()
    print("主")



