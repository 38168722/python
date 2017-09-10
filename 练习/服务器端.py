#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 15:56
# @Author  : Aries
# @Site    : 
# @File    : 服务器端.py
# @Software: PyCharm
import struct
import socket
import subprocess
server =socket.socket()
server.bind(("192.168.20.30",8080))
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.listen(5)
while True:
    print("alrady starting.....")
    conn,client_addr=server.accept()
    while True:
        try:
            print("client_addr:",client_addr)
            client_msg=conn.recv(1024)
            res=subprocess.Popen(client_msg.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()
            du=len(stdout)+len(stderr)
            print(du)
            header=struct.pack("i",du)
            conn.send(header)
            conn.send(stdout+stderr)
        except Exception:
            break
    conn.close()
server.close()
