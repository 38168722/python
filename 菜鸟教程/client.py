#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 17:16
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.connect(('192.168.2.132',8088)) #绑定手机卡

#发，收消息
while True:
    cmd=input('>>: ').strip()
    print(cmd)
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    cmd_res=phone.recv(1024)
    print(cmd_res.decode('gbk'))
phone.close()