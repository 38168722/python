#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 14:11
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
import struct
import json
client=socket.socket()
client.connect(("localhost",8080))
while True:
    msg=input(">>:").strip()
    if not msg:continue
    client.send(msg.encode("utf-8"))
    header_len=struct.unpack("i",client.recv(4))[0]
    header_bytes=client.recv(header_len)
    header_json=header_bytes.decode("utf-8")
    header_dic=json.loads(header_json)
    total_size=header_dic['total_size']

    recv_size=0
    total_data=b''
    while recv_size<total_size:
        recv_data=client.recv(1024)
        recv_size+=len(recv_data)
        total_data+=recv_data
    print(total_data.decode("gbk"))
client.close()