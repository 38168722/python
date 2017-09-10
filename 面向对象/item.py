#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 19:27
# @Author  : Aries
# @Site    : 
# @File    : item.py
# @Software: PyCharm
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __getitem__(self, item):
#         return getattr(self,item)
#     def __setitem__(self, key, value):
#         setattr(self,key,value)
#     def __delitem__(self, key):
#         self.__dict__.pop(key)
# f=Foo("egon",18)
# f["sex"]="woman"
# print(len(f))

# print("============>1")
# try:
#     num=input(">>:")
#     int(num)
#     print("dict----->>")
#     print("dict----->>")
#     print("dict----->>")
#     print("dict----->>")
#     d={'a':1}
#     d['b']
# except ValueError:
#     print("=====>")
# print("======:>2")
# import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s -- %(message)s'
# )
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("出错了")
# import logging
# logger=logging.getLogger()
# file_handler=logging
# x=2
# y=20
# print("afdsafdsa")
# assert x>y
# print("hello world")
class EgonException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

raise EgonException("出错啦")