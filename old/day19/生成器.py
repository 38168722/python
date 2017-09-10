#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/4 8:23
# @Author  : Aries
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm
import time
def tail(filename):
    f = open(filename,encoding="utf-8")
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
tail_g=tail('作业.py')
for line in tail_g:
    print(line)