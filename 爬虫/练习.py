#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 9:55
# @Author  : Aries
# @Site    : 
# @File    : 练习.py
# @Software: PyCharm
import shelve

f = shelve.open("shelve_file")
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}
# f.close()
existing=f['key']
f.close()
print(existing)


