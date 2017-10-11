#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def print_mg(msg):
#     print(msg)
#
# print_mg("hello world")

# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# print(max2(3,4))

# def foo(x,y):
#     return x+y
# print(foo(1,2))

# def func(x,y,**kwargs):
#     print(x,y)
#     print(kwargs)
#
# def func(x,y,*args):
#     print(x,y)
#     print(args)
#
# func(1,2,3,4,5,6)


def delete():
    print("delete func")

def change():
    print("change func")

def add():
    print("add func")

def check():
    print("check func")

func_dic={
    "select":select,
    "delete":delete,
    "change":change,
    "add":add,
    "check":check,

}


