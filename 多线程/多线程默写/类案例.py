#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 22:43
# @Author  : Aries
# @Site    : 
# @File    : 类案例.py
# @Software: PyCharm
from multiprocessing import Process
import os,time
class Person(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print("%s start piaoing.."%self.name)
        print(os.getppid(),os.getpid())
        time.sleep(5)


if __name__ == '__main__':
    p1=Person("wupeiqi")
    p2=Person("yuanhao")
    p3=Person("egon")
    p1.start()
    p2.start()
    p3.start()


