#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 17:08
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
import time,select
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8080))
server.listen(5)
server.setblocking(False)
print("starting....")
reads_l=[server,]
while True:
    r_l,_,_=select.select(reads_l,[],[])
    print(r_l)
    for obj in r_l:
        if obj==server:
            conn,addr=obj.accept()
            reads_l.append(conn)
        else:
            data=obj.recv(1024)
            obj.send(data.upper())