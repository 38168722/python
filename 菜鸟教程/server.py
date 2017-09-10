#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 17:15
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8082)) #绑定手机卡
phone.listen(5) #开机

print('starting...')
while True: #链接循环
    conn,client_addr=phone.accept() #等电话 （链接，客户的的ip和端口组成的元组）
    print('-------->',conn,client_addr)

    #收，发消息
    while True:#通信循环
        try:
            cmd=conn.recv(1024)
            if not cmd:break #针对linux
            #执行cmd命令，拿到cmd的结果，结果应该是bytes类型
            #。。。。
            res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()

            #发送命令的结果
            conn.send(stdout+stderr)
        except Exception:
            break
    conn.close() #挂电话
phone.close() #关机



