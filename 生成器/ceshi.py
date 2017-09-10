#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 19:14
# @Author  : Aries
# @Site    : 
# @File    : ceshi.py
# @Software: PyCharm
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
#
# @init
# def eater(name):
#     print("%s ready to eat"%name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         food_list.append(food)
#         print("%s start to eat %s"%(name,food))
#
#
# def make_shit(people,n):
#     for i in range(n):
#        print(people.send(i))
#
# e=eater("alex")
# make_shit(e,5)

import os
# g=os.walk(r"E:\baiduyun")
# for par_dir,_,files in g:
#     for file in files:
#         file_path=r'%s\%s'%(par_dir,file)
#         # print(file_path)
#         with open(file_path,encoding="utf-8") as fr:
#             for i in fr:
#                 if "root" in i:
#                     print(file_path)
#                     break

def search(target,start_path):
    g=os.walk(start_path)
    for par_dir,_,files in g:
        for file in files:
            file_path=r'%s\%s'%(par_dir,file)
            target.send(file_path)

@init
def opener(target):
    while True:
        file_path=yield
        with open(file_path,encoding="utf-8") as f:
            target.send((file_path,f))
@init
def cat(target):
    while True:
        filepath,f=yield
        for line in f:
            res=target.send((filepath,line))
            if res:
                break
@init
def grep(target,pattern):
    tag=False
    while True:
        tag=False
        filepath,line=yield tag
        if pattern in line:
            target.send(filepath)
            tag=True
@init
def printer():
    while True:
        filename=yield
        print(filename)
start_path=r"E:\baiduyun"
search(opener(cat(grep(printer(),"root"))),start_path)