#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 11:52
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
import subprocess
import struct
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8088))
print("starting...")
while True:
    msg,client_addr=server.recvfrom(1024)
    print("client_addr",client_addr)
    res=subprocess.Popen(msg.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout=res.stdout.read()
    stderr=res.stderr.read()
    header_info=struct.pack("i",len(stderr)+len(stdout))
    server.sendto(header_info,client_addr)
    server.sendto(stdout+stderr,client_addr)
server.close()