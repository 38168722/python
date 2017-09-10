#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 20:08
# @Author  : Aries
# @Site    : 
# @File    : md5模块.py
# @Software: PyCharm
import hashlib
md5=hashlib.md5()
md5.update(b"hello")
print(md5.hexdigest())