#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 9:21
# @Author  : Aries
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
from threading import Thread
msg_l=[]
format_l=[]
def talk():
    while True:
        msg=input("=>>")
        if not msg:continue
        msg_l.append(msg)

def format_str():
    while True:
        if msg_l:
            format_l.append(msg_l.pop().upper())

def save():
    while True:
        if format_l:
            f=open("db.txt","a")
            f.write("%s\n"%format_l.pop())
            f.flush()
            f.close()

if __name__ == '__main__':
    Thread(target=talk).start()
    Thread(target=format_str).start()
    Thread(target=save).start()

