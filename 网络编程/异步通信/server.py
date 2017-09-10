#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 10:58
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
from multiprocessing import pool
server=socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8080))
server.listen(5)

def talk(conn,addr):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
        conn.close()

