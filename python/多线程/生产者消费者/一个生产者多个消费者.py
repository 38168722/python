#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/26 11:21
# @Author  : Aries
# @Site    : 
# @File    : 一个生产者多个消费者.py
# @Software: PyCharm
# from multiprocessing import Process,Queue
# import time,random
# def consumer(q):
#     while True:
#         str=q.get()
#         if str is None:break
#         print("消费者吃%s"%str)
#         time.sleep(random.randint(1,3))
#
# def producer(seq,q):
#     for item in seq:
#         q.put(item)
#         print("生产都做%s"%item)
# if __name__ == '__main__':
#     q=Queue()
#     producer(("包子%s"%i for i in range(10)),q)
#     p1=Process(target=consumer,args=(q,))
#     p1.start()
#     q.put(None)

#
# from multiprocessing import Process,JoinableQueue
# import time,random,os
# def consumer(q):
#     while True:
#         res=q.get()
#         time.sleep(random.randint(1,3))
#         print("%s吃%s"%(os.getpid(),res))
#         q.task_done()
#
# def producer(name,q):
#     for i in range(10):
#         time.sleep(random.randint(1,3))
#         res="%s%s"%(name,i)
#         q.put(res)
#         print("%s生产了%s"%(os.getpid(),res))
#     q.join()
#
# if __name__ == '__main__':
#     q=JoinableQueue()
#     p1=Process(target=producer,args=("包子",q))
#     p2=Process(target=producer,args=("骨头",q))
#     p3=Process(target=producer,args=("泔水",q))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,))
#     c2=Process(target=consumer,args=(q,))
#     c1.daemon=True
#     c2.daemon=True
#
#     #开始
#     p_l=[p1,p2,p3,c1,c2]
#     for p in p_l:
#         p.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print("主")
from multiprocessing import Manager,Process,Lock
import os
def work(d,lock):
    d["count"]-=1

if __name__ == '__main__':
    lock=Lock()
    with Manager() as m:
        dic=m.dict({"count":100})
        p_l=[]
        for i in range(100):
            p=Process(target=work,args=(dic,lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)


