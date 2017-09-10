#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 11:19
# @Author  : Aries
# @Site    : 
# @File    : pickle模块.py
# @Software: PyCharm
import pickle
# dic={"name":"wuhao","age":32}
# f = open("pickle.txt","wb")
# pickle.dump(dic,f)

f = open("pickle.txt","rb")
print(pickle.loads(f.read()))