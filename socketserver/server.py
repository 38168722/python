#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 9:14
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socketserver
class MyTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data=self.request.recv(1024)
                if not data:break
                self.request.send(data.upper())
            except Exception:
                break
        self.request.close()
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),MyTCPhandler)
    server.allow_reuse_address=True
    server.serve_forever()
