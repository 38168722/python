#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 22:35
# @Author  : Aries
# @Site    : 
# @File    : phone_client.py
# @Software: PyCharm
import socket
client=socket.socket()
client.connect(("127.0.0.1",8080))
while True:
    msg=input("=>>")
    if not msg:continue
    client.send(msg.encode("utf-8"))
    server_message=client.recv(1024)
    print(server_message.decode("gbk"))