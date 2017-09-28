#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 8:24
# @Author  : Aries
# @Site    : 
# @File    : 内置方法.py
# @Software: PyCharm
# try:
#     x
#     print('=======)
#     int('abc')
#     l = []
#     l[10000]
#     class Foo:pass
#     Foo.x
#     1/0
#     dic = {'k':'v'}
#     dic['k2']
# except Exception as e:
#     print("出错啦")
#
# print("还在继续运行吗")


# class EgonException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# try:
#     raise EgonException("egon 出异常了")
# except EgonException as e:
#     print(e)

# import hashlib
# user="alex"
# pwd="3713"
# md5_obj=hashlib.md5(user.encode("utf-8"))
# md5_obj.update(pwd.encode("utf-8"))
# print(md5_obj.hexdigest())
# import hashlib
# md5_obj=hashlib.md5()
# import os
# filename="abc.txt"
# filesize=os.path.getsize(filename)
# print(filesize)
# f=open(filename,'rb')
# while filesize>0:
#     if filesize>1024:
#         content=f.read(1024)
#         filesize-=1024
#     else:
#         content=f.read(filesize)
#         print("content===",content)
#         filesize-=filesize
#         print("filesize=====",filesize)
#     md5_obj.update(content)

# class Teacher:
#     school="shanghai"
#     def walk(self):
#         print("我在走路")
#
# t=Teacher()
# t.school="fdsafdsafdsafsa"
# print(t.__dict__)


# class Cmd:
#     def __init__(self,name):
#         self.name=name
#     def run(self):
#         while True:
#             cmd = input(">>:").strip()
#             # if not cmd:continue
#             if hasattr(self,cmd):
#                 func=getattr(self,cmd)
#                 func()
#             else:
#                 print("not valid func")
#
#     def ls(self):
#         print("ls funciton")
#
# c=Cmd("egon")
# c.run()



# class Cmd:
#     def __init__(self,name):
#         self.name=name
#
#     def run(self):
#         while True:
#             cmd=input("==>>")
#             if hasattr(self,cmd):
#                 func=getattr(self,cmd)
#                 func()
#             else:
#                 print("invalid command")
#     def ls(self):
#         print("ls function is printInfo")
#
#
#
# test=Cmd("egon")
# test.run()
#

# class Teacher:
#     def __init__(self,name):
#         self.name=name
#         self.courses=[]
#
#
#     def __str__(self):
#         return "<<name:%s>>"%self.name
#
# class Course:
#     def __init__(self,name,price,period):
#         self.name=name
#         self.price=price
#         self.period=period
#
#     def __str__(self):
#         return "<name:%s price:%s>"%(self.name,self.price)
#
# # c1=Course("egon",99999,6)
# # print(c1)
# t=Teacher("nelsone")
# print(t)



