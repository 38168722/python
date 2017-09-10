#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 10:38
# @Author  : Aries
# @Site    : 
# @File    : 异步进程池.py
# @Software: PyCharm
from multiprocessing import Pool
import os,time,random
def task(n):
    print("<%s> is running"%os.getpid())
    time.sleep(random.randint(1,3))
    return n**2
if __name__ == '__main__':
    p=Pool(4)
    obj_l=[]
    for i in range(1,21):
        obj=p.apply_async(task,args=(i,))
        obj_l.append(obj)
    p.close()
    p.join()
    print("主线程")
    for obj in obj_l:
        print(obj.get())