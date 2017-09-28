#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 15:30
# @Author  : Aries
# @Site    : 
# @File    : 测试一.py
# @Software: PyCharm
# from urllib.request import urlopen
# def index(url):
#     def get():
#         return urlopen(url).read()
#     return get
# baidu=index("http://www.baidu.com")
# print(baidu().decode("utf-8"))

# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print("run time is %s"%(stop_time-start_time))
#         return res
#     return wrapper
#
# @timmer
# def foo():
#     time.sleep(3)
#     print("from foo")
# foo()


def auth(driver="file"):
    def auth2(func):
        def wrapper(*args,**kwargs):
            name=input("user:")
            pwd=input("pwd:")
            if driver=="file":
                if name=="egon" and pwd=="123":
                    print("login successful")
                    res=func(*args,**kwargs)
                    return res
            elif driver=="ldap":
                print("ldap")
        return wrapper
    return auth2

@auth(driver="file")
def foo(name):
    print(name)

foo("egon")