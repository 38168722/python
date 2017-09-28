#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 17:09
# @Author  : Aries
# @Site    : 
# @File    : server1.py
# @Software: PyCharm
import socket
import subprocess
server = socket.socket()
server.bind(("127.0.0.1",8080))
server.listen(5)
while True:
    print("starting.....")
    conn,client_addr=server.accept()
    print("client_addr",client_addr)
    while True:
        client_addr=conn.recv(1024)
        res=subprocess.Popen(client_addr.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout=res.stdout.read()
        stderr=res.stderr.read()
        conn.send(stderr+stdout)
    conn.close()
server.close()