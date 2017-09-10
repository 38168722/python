#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 10:10
# @Author  : Aries
# @Site    : 
# @File    : 进程池.py
# @Software: PyCharm
from multiprocessing import Pool
import os,time
def task(n):
    print("<%s> is running"%os.getpid())
    time.sleep(2)
    print("<%s> is done"%os.getpid())
    return n**2
if __name__ == '__main__':
    p=Pool(4)
    for i in range(1,7):
        res=p.apply(task,args=(i,))
        print("本次任务的结果:%s"%res)
    print("主")

print("cpu个数是%s"%os.cpu_count())