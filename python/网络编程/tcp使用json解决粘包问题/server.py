#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 14:11
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket
import subprocess
import json
import struct
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("localhost",8080))
server.listen(5)
while True:
    print("starting.....")
    conn,client_addr=server.accept()
    print("client_addr",client_addr)
    while True:
            cmd=conn.recv(1024)
            res=subprocess.Popen(cmd.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()
            header_info={
                "total_size":len(stdout)+len(stderr),
                "filename":None,
                "md5":None
            }
            header_json=json.dumps(header_info)
            header_bytes=header_json.encode("utf-8")
            conn.send(struct.pack("i",len(header_bytes)))
            conn.send(header_bytes)
            conn.send(stdout)
            conn.send(stderr)
    conn.close()
server.close()
