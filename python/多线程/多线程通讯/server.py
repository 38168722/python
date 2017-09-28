#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 10:52
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
from multiprocessing import Process
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",8088))
s.listen(5)
def talk(conn,addr):
    while True:
        try:
            print(conn,addr)
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
if __name__ == '__main__':
    while True:
        conn,addr=s.accept()
        p=Process(target=talk,args=(conn,addr))
        p.start()
    s.close()

