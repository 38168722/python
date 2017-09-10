#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 9:49
# @Author  : Aries
# @Site    : 
# @File    : 购票升级版.py
# @Software: PyCharm
from multiprocessing import Process,Lock
import json,time,random,os
def search():
    dic=json.load(open("db.txt",))
    print("剩余票数%s"%dic["count"])

def get_ticket():
    dic=json.load(open("db.txt",))
    if dic["count"]>0:
        dic["count"]-=1
        time.sleep(random.randint(1,3))
        json.dump(dic,open("db.txt","w"))
        print("%s 购票成功"%os.getpid())

def task(mutex):
    search()
    mutex.acquire()
    get_ticket()
    mutex.release()
if __name__ == '__main__':
    mutex=Lock()
    for i in range(50):
        p=Process(target=task,args=(mutex,))
        p.start()
