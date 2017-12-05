#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def application(environ, start_response):
    print("server is starting....")
    start_response('200 OK',[('Content-Type', 'text/html')])
    print("environ===",environ.get("PATH_INFO"))
    print("是啥数据类型",type(environ.get("PATH_INFO")))
    if environ.get("PATH_INFO") == "/login":
        # f=open("login.html","rb")
        # data = f.read()
        return [b"jjj"]
    # return [b"hello"]

    if environ.get("PATH_INFO")=="/favicon.ico":
        return [b"the page is error"]

httpd = make_server('127.0.0.1',8082,application)
httpd.serve_forever()
