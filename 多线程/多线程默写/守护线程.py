#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 10:44
# @Author  : Aries
# @Site    : 
# @File    : 守护线程.py
# @Software: PyCharm
from multiprocessing import Process,JoinableQueue
import time,random
def consumer(name,q):
    while True:
        print("进来了没")
        time.sleep(random.randint(1,2))
        res=q.get()
        print('%s拿到了 %s' %(name,res))
        q.task_done()

def producer(seq,q):
    for item in seq:
        time.sleep(random.randrange(1,2))
        q.put(item)
        print('生产者做好了 %s' %item)
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    seq=('包子%s' %i for i in range(10))
    p1=Process(target=consumer,args=('消费者1',q,))
    p1.daemon=True
    p1.start()
    producer(seq,q)
    print('主线程')
