#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 9:35
# @Author  : Aries
# @Site    : 
# @File    : 测试一.py
# @Software: PyCharm
from multiprocessing import Manager,Process,Lock
def work(dic,mutex):
    with mutex:
        dic["count"]-=1

if __name__ == '__main__':
    mutex=Lock()
    m=Manager()
    share_dic=m.dict({"count":100})
    p_1=[]
    for i in range(100):
        p=Process(target=work,args=(share_dic,mutex))
        p_1.append(p)
        p.start()
    for i in p_1:
        i.join()
    print(share_dic)