#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 13:55
# @Author  : Aries
# @Site    : 
# @File    : udpserver.py
# @Software: PyCharm
from socket import *
client = socket(AF_INET,SOCK_STREAM)
ip_port=("127.00.1",8080)
name=input(">>").strip()
client.sendto(name.encode("utf-8"),ip_port)
data,addr=client.recvfrom(1024)
print(data.decode("utf-8"))