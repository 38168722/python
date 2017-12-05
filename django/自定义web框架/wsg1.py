#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response("200 OK",[('Content-Type','text/html')])
    url=environ['PATH_INFO']
    print("url----",url)
    f = open("index.html")
    data=f.read()
    print(data)
    if url=="/index":
        return [data.encode("GBK")," "]
    # return [b'<h1>Hello Yuan</h1>',]


s=make_server("127.0.0.1",8080,application)
print("server is working...")
s.serve_forever()