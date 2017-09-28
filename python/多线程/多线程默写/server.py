#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 19:45
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
from multiprocessing import Process
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8080))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            cmd=conn.recv(1024)
            conn.send(cmd.upper())
        except Exception:
            break
    conn.close()

if __name__ == '__main__':
    while True:
        print("starting......")
        conn,client_adr=server.accept()
        print("client_addr",client_adr)
        p=Process(target=talk,args=(conn,client_adr))
        p.start()
    server.close()