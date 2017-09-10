#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 17:17
# @Author  : Aries
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import os
test=os.popen("dir").read()
print("是什么类型",type(test))