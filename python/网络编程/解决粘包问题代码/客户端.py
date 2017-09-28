#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 13:08
# @Author  : Aries
# @Site    : 
# @File    : 客户端.py
# @Software: PyCharm
import socket
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.connect(('192.168.20.51',8080)) #绑定手机卡

#发，收消息
while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    #先收报头
    header_struct=phone.recv(4)
    unpack_res = struct.unpack('i', header_struct)
    print("报头类型",type(unpack_res))
    total_size=unpack_res[0]

    #再收数据
    recv_size=0 #10241=10240+1
    total_data=b''
    while recv_size < total_size:#1    0 1025
        recv_data=phone.recv(1024)
        recv_size+=len(recv_data)
        total_data+=recv_data
    print(total_data.decode('gbk'))
phone.close()