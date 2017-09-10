#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 15:56
# @Author  : Aries
# @Site    : 
# @File    : 客户端.py
# @Software: PyCharm
import socket
import struct
client=socket.socket()
client.connect(("127.0.0.1",8080))
while True:
    msg=input("=>>")
    if not msg:continue
    client.send(msg.encode("utf-8"))
    header_struct=client.recv(4)
    # print(type(header_struct),len(header_struct))
    total_size=struct.unpack("i",header_struct)[0]
    # total_size=header_size[0]
    print("total_size",total_size)
    server_msg=client.recv(total_size)
    print(server_msg.decode('gbk'))

client.close()