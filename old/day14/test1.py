#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 13:03
# @Author  : Aries
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

# url_l = []
# from urllib.request import urlopen
#
# def get_cache(func):
#     def inner(*args,**kwargs):
#         url = args[0]
#         filename = str(hash(url))
#         if url in url_l:
#             f = open(filename,'rb')
#             print("从缓存里取值")
#             ret = f.read()
#         else:
#             print("从网上下载")
#             url_l.append(url)
#             ret = func(*args, **kwargs)
#             f = open(filename,'wb')
#             f.write(ret)
#         f.close()
#         return ret
#     return inner
#
# @get_cache
# def get(url):
#     return urlopen(url).read()
#
# print(get('http://www.cnblogs.com/linhaifeng'))
# print(get('http://www.cnblogs.com/linhaifeng'))
# print(get('http://www.cnblogs.com/linhaifeng'))
# print(get('http://www.cnblogs.com/linhaifeng'))
# print(get('http://www.cnblogs.com/linhaifeng'))
# list2=['http://www.qq.com','http://www.baidu.com']
# list2.append('http://www.google.com')
# print(list2)
flag=False
def outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                print("方法执行前")
            ret=func()
            if flag:
                print("方法执行后")
            return ret
        return inner
    return timer

@outer(flag)
def index():
    print("======welcome=======")

index()