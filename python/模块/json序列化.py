#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 10:32
# @Author  : Aries
# @Site    : 
# @File    : json序列化.py
# @Software: PyCharm
import json
# dic={"name":"wuhao","age":32}
# f=open("json_data.txt","w")
# data=json.loads(f)
# print(data)
dic={"name":"wuhao","age":32}
f = open("json_data.txt","r")
dic=json.load(f)
print(dic)