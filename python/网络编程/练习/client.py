#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 13:29
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
ip_port=("127.0.0.1",8080)
bufsize=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input(">>:").strip()
    if not msg:continue
    client.sendto(msg.encode("utf-8"),ip_port)
    back_msg,addr=client.recvfrom(bufsize)
    print(back_msg.decode("utf-8"),addr)