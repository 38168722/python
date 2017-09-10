#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 7:55
# @Author  : Aries
# @Site    : 
# @File    : 高阶函数.py
# @Software: PyCharm
# def foo():
#     print("我的函数名作为参数传给高阶函数")
#
# def gao_jie1(func):
#     print("我是高阶函数1,我接收的参数是%s"%func)
#     func()
#
# def gao_jie2(func):
#     print("我是高阶函数2,我的返回值是%s"%func)
#     return func
#
# gao_jie1(foo)
# gao_jie2(foo)

# def father(name):
#     print("from father %s"%name)
#     def son():
#         print('from son')
#         def grandson():
#             print("from grandson")
#         grandson()
#     son()
# father("abc")


# def length(name):
#     count=0
#     for i in name:
#         count+=1
#     return count
#
# print(length("helllo world wo cao"))
#
# def list1(name):
#     return name[-1]
#
# print(list1(['1','2']))

# while True:
#     name = input("please input your name")
#     if not name:continue
#     print("login success")
#     break


# def max(a1,a2):
#     if a1>a2:
#         return a1
#     else:
#         return a2
#
# print(max(a1=100,a2=999))


# def check_login(name,password="123"):
#     if name=="egon" and password=="123":
#         return True
#     else:
#         return False
#
# if check_login("egon"):
#     print("登录成功")
# else:
#     print("登录失败")
#
# def max_value(a,b=3):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(max_value(8))

# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         stop_time=time.time()
#         print('函数[%s],运行时间是[%s]'%(func,stop_time-start_time))
#     return wrapper
#
# @timer
# def cal(array):
#     res=0
#     for i in array:
#         res+=i
#     return res
#
# cal(range(10))

# user_list=[
#     {'name':'alex','passwd':'123'},
#     {'name':'linhaifeng','passwd':'123'},
#     {'name':'wupeiqi','passwd':'123'},
#     {'name':'yuanhao','passwd':'123'},
# ]
#
# current_user={'username':None,'login':False}
#
# def auth_deco(func):
#     def wrapper(*args,**kwargs):
#         if current_user['username'] and current_user['login']:
#             res=func(*args,**kwargs)
#             return res
#         username=input('用户名:').strip()
#         passwd=input('密码:').strip()
#
#         for index,user_dic in enumerate(user_list):
#

import time
# def foo():
#     print('from the foo')
#
# def timmer(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print("函数%s运行时间是%s"%(func,stop_time-start_time))
#
# timmer(foo)

# def father(name):
#     def son():
#         def grandson():
#             print('from grandson %s'%name)
#         return grandson
#     return son
#
# f = father("nelsone")
# print(f()())



