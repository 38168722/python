#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 13:56
# @Author  : Aries
# @Site    : 
# @File    : udpclient.py
# @Software: PyCharm
from socket import *
ip_port = ('127.0.0.1',8080)
server = socket(AF_INET,SOCK_DGRAM)
server.bind(ip_port)
data1,addr = server.recvfrom(222)
# data2,addr2 = server.recvfrom(10)
print('---->',data1.decode('utf-8'))
# print('---->',data2.decode('utf-8'))
