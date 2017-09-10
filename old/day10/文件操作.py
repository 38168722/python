#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 16:47
# @Author  : Aries
# @Site    : 
# @File    : 文件操作.py
# @Software: PyCharm
#问题代码a+ 模式无法边读边写
# with open("sss.jpg",'rb') as read_file,open("hello.jpg",'wb') as write_file:
#     for line in read_file:
#         write_file.write(line)
while True:
    name = input("请输入你的名字")
    password = input("请输你的密码")
    if name and password:continue
    print("login success")
    break



# import os
# with open("test1","r",encoding='utf-8') as read_file,open('test2','w',encoding='utf-8') as write_file:
#     for i in read_file:
#         write_file.write(i.replace("社会主义","资本主义"))
#     read_file.close()
#     os.remove("test1")
#     os.rename("test2","test1")