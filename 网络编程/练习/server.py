#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 13:29
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
bufsize=1024
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",8080))
while True:
    msg,addr=server.recvfrom(bufsize)
    print(msg,addr)
    server.sendto(msg.upper(),addr)
