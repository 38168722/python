#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 11:53
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
import struct
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input(">>:").strip()
    client.sendto(msg.encode("utf-8"),("127.0.0.1",8088))
    header_size=struct.unpack("i",client.recv(4))[0]
    res,server_addr=client.recvfrom(header_size)
    print(res.decode("gbk"))
client.close()