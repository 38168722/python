#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 14:14
# @Author  : Aries
# @Site    : 
# @File    : make_shit.py
# @Software: PyCharm
def init(func):
    def wrapper(*args,**kwargs):
        ret = func(*args,**kwargs)
        next(ret)
        return ret
    return wrapper
@init
def foo():
    print('starting')
    while True:
        x=yield None
        print("value: ",x)

# g=foo()
# g.send(10)
# g.send(20)

@init
def eater(name):
    print("%s ready to eat"%name)
    food_list=[]
    while True:
        food=yield food_list
        food_list.append(food)
        print("%s ready to eat %s"%(name,food))

e=eater("alex")


def make_shit(people,n):
    for i in range(n):
        people.send('shit%s'%i)

make_shit(e,5)
#应用：grep -rl 'root' /etc
import os
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
#阶段一：递归地找文件的绝对路径，把路径发给阶段二
@init
def search(target):
    'search file abspath'
    while True:
        start_path=yield
        g = os.walk(start_path)
        for par_dir, _, files in g:
            # print(par_dir,files)
            for file in files:
                file_path = r'%s\%s' % (par_dir, file)
                target.send(file_path)
#阶段二：收到文件路径，打开文件获取获取对象，把文件对象发给阶段三
@init
def opener(target):
    'get file obj: f=open(filepath)'
    while True:
        file_path=yield
        with open(file_path,encoding='utf-8') as f:
            target.send((file_path,f))

#阶段三：收到文件对象，for循环读取文件的每一行内容，把每一行内容发给阶段四
@init
def cat(target):
    'read file'
    while True:
        filepath,f=yield
        for line in f:
            res=target.send((filepath,line))
            if res:
                break

#阶段四：收到一行内容，判断root是否在这一行中，如果在，则把文件名发给阶段五
@init
def grep(target,pattern):
    'grep function'
    tag=False
    while True:
        filepath,line=yield tag #target.send((filepath,line))
        tag=False
        if pattern in line:
            target.send(filepath)
            tag=True
#阶段五：收到文件名，打印结果
@init
def printer():
    'print function'
    while True:
        filename=yield
        print(filename)
#
# start_path1=r'C:\Users\SKY\PycharmProjects\作业'
# start_path2=r'C:\Users\SKY\PycharmProjects\作业'
g=search(opener(cat(grep(printer(),'root'),start_path1)))
#
# print(g)
# # g.send(start_path1)
# g.send(start_path2)

# @init
# def func():
#     tag=False
#     while True:
#         x=yield tag
#         if 'root' in x:
#             print(x)
#             tag=True
# g=func()
# # print(g.send('a'))
# print(g.send('root123'))
#
# def ceshi():
#     print("hello world")
#     print("fuck you baba")
#     abc=yield
#     print(abc)
#
# while True:
#     g=ceshi()
# next(g)
# g.send(10)
# import math
# class circular:
#     def __init__(self,zhijing,banjing):
#         self.zihjing=zhijing
#         self.banjing=banjing
#     def mianji(self):
#         print(3.14*math.sqrt(self.banjing))
#     def zhouchang(self):
#         print(2*3.14*self.banjing)

# def eat(name):
#     print("%s开始吃东西了"%name)
#     tag=False
#     while True:
#         food=yield tag
#         if food=='shit':
#             tag=True
#         print("%s吃%s"%(name,food))
#
# g=eat("alex")
# next(g)
# g.send("面")
# g.send("饭")
# print(g.send("鸡腿"))
# print(g.send("shit"))
#



