#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 11:02
# @Author  : Aries
# @Site    : 
# @File    : Queue.py
# @Software: PyCharm
from multiprocessing import process,Queue
import time,random
q=Queue(3)
q.put("first")
q.put("second")
q.put("third")
print(q)
for i in range(1,4):
    print(q.get())