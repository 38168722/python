#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 15:33
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8080))

while True:
    msg=input(">>:").strip()
    if not msg:continue
    s.send(msg.encode("utf-8"))
    data=s.recv(1024)
    print(data)