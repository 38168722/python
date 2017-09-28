#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 9:32
# @Author  : Aries
# @Site    : 
# @File    : 购票案例.py
# @Software: PyCharm
from multiprocessing import Process,Lock
import json
import time
import random
import os
def task(mutex):
    dic=json.load(open("db.txt"))
    print("剩余票数%s"%dic["count"])
    mutex.acquire()
    dic=json.load(open("db.txt",))
    if dic["count"]>0:
        dic["count"]-=1
        time.sleep(random.randint(1,3))
        json.dump(dic,open("db.txt","w"))
        print("%s购票成功"%os.getpid())
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(50):
        p=Process(target=task,args=(mutex,))
        p.start()