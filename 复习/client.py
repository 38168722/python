#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 17:08
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
client=socket.socket()
client.connect(("127.0.0.1",8080))
while True:
    cmd=input(">>")
    if not cmd:continue
    client.send(cmd.encode("utf-8"))
    data=client.recv(1024)
    print(data.decode("utf-8"))