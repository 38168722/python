#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import urls

def application(environ,start_response):
    start_response("200 OK",[('Content-Type','text/html')])
    path=environ.get("PATH_INFO")
    URLpattern=urls.URLpattern
    print("URLpattern",URLpattern)
    func=None
    for item in URLpattern:
        if path==item[0]:
            func=item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [b"<h1>404</h1>"]

s=make_server("127.0.0.1",8083,application)