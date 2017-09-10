#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 20:11
# @Author  : Aries
# @Site    : 
# @File    : 类案例.py
# @Software: PyCharm
from multiprocessing import Process
import time,random
import os
class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print("%s is piaoing...."%self.name)
        print(os.getppid(),os.getpid())
        time.sleep(10)


if __name__ == '__main__':
    p1=Piao("alex")
    p2=Piao("wupeiqi")
    p3=Piao("yuanhao")
    p1.start()
    p2.start()
    p3.start()
    print("主进程",os.getpid(),os.getppid())