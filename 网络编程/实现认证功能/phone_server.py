#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 22:35
# @Author  : Aries
# @Site    : 
# @File    : phone_server.py
# @Software: PyCharm
import socket
import subprocess

def warrp(func):
    def inner(*args,**kwargs):
        ret=func(*args,**kwargs)
        return ret
    return inner



def server():
    server = socket.socket()
    server.bind(("127.0.0.1",8080))
    server.listen(5)
    while True:
        print("starting.....")
        conn,client_addr=server.accept()
        print("client_addr",client_addr)
        while True:
            client_addr=conn.recv(1024)
            res=subprocess.Popen(client_addr.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()
            conn.send(stderr+stdout)
            print("有没有运行到这里")
        conn.close()
    server.close()


