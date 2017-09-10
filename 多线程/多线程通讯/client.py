#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 10:52
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
c=socket.socket()
c.connect(("127.0.0.1",8088))
while True:
    msg=input(">>:").strip()
    if not msg:continue
    c.send(msg.encode("utf-8"))
    data=c.recv(1024)
    print(data.decode("utf-8"))
c.close()