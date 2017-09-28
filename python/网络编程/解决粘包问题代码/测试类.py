#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 15:02
# @Author  : Aries
# @Site    : 
# @File    : 测试类.py
# @Software: PyCharm
import struct
res=struct.pack("i",777777)
print("res的类型",type(res))
abc=struct.unpack("i",res)
print(abc[0])