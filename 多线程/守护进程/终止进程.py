#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 10:41
# @Author  : Aries
# @Site    : 
# @File    : 终止进程.py
# @Software: PyCharm
from multiprocessing import Process
import os,time
def work():
    print("%s is working"%os.getpid())
    time.sleep(3)
if __name__ == '__main__':
    p1=Process(target=work)
    # p2=Process(target=work)
    # p3=Process(target=work)
    # p1.daemon=True
    # p2.daemon=True
    # p3.daemon=True
    p1.start()
    p1.terminate()
    time.sleep(3)
    print(p1.is_alive())
    # p2.start()
    # p3.start()

    # p3.join()
    p1.join()
    # p2.join()
    print("基于初始化的结果继续运行")

