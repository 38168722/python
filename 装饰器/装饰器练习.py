#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 15:43
# @Author  : Aries
# @Site    : 
# @File    : 装饰器练习.py
# @Software: PyCharm
import random
import time


#统计时间功能
# def timmer(func):
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         ret=func(*args,**kwargs)
#         stop_time=time.time()
#         print("一共运行了%s秒"%(stop_time-start_time))
#         return ret
#     return inner
#
# @timmer
# def foo():
#     print("starting is execute")
#     time.sleep(random.randint(1,10))
#     print("stopped is now")
#
# foo()

#认证功能

# def auth(func):
#     def inner(*args,**kwargs):
#         if args[0]=="egon" and args[1]=="123":
#             print("welcome to myhome")
#             res=func(*args,**kwargs)
#             return res
#         else:
#             print("login error")
#     return inner
# @auth
# def foo(name,password):
#     print("机器人函数")
# foo("egon","33")
# import json
# def readfile(name):
#     f=open(name,"r",encoding="utf-8")
#     return json.loads(f.read())
#
# auth_file=readfile(r"C:\Users\SKY\PycharmProjects\装饰器\auth")
# user_state={
#     "user":None,
#     "state":False
# }



#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         if user_state["state"]==False:
#             name=input("name:").strip()
#             password=input("password:").strip()
#             if name==auth_file.get("name") and password==auth_file.get("password"):
#                 user_state["user"]=name
#                 user_state["state"]=True
#                 ret=func(*args,**kwargs)
#                 print("login auth successful")
#         else:
#             ret=func(*args,**kwargs)
#             print("login end....")
#             return ret
#
#     return inner
#
# def timmer(func):
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         if stop_time-start_time>5:
#             user_state["state"]=False
#         return res
#     return inner
#
# @wrapper
# @timmer
# def printInfo():
#     print("print execute start")
#     time.sleep(random.randint(1,6))
#     print("print execute end")
# printInfo()
# printInfo()
# printInfo()
#六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# from urllib.request import urlopen
#
# def get_url(url):
#     def inner():
#         ret=urlopen(url).read().decode("utf-8")
#         print(ret)
#     return inner
#
# baidu=get_url("http://www.baidu.com")
# baidu()
# baidu()

#七：为题目五编写装饰器，实现缓存网页内容的功能：

# import os,hashlib
# from urllib.request import urlopen
# def check_file(file_name,content):
#     if not os.path.exists(file_name):
#         print("缓存里无直接写进去")
#         with open(file_name,"w",encoding="utf-8") as f:
#             f.write(content)
#         print("写入成功!!!")
#     else:
#         print("直接从缓存里拿")
#         with open(file_name,"r",encoding="utf-8") as f:
#             f.read()
# def geturl(url):
#     def inner():
#         md5=hashlib.md5()
#         md5.update(url.encode("utf-8"))
#         filename=md5.hexdigest()
#         content=urlopen(url).read().decode("utf-8")
#         check_file(filename,content)
#     return inner
#
# baidu=geturl("http://www.baidu.com")
# sogou=geturl("http://www.sogou.com")
# sogou()
#题目八,做一个高大上的字典

# route_dic={}
# def make_route(name):
#     def deco(func):
#         route_dic[name]=func
#     return deco
# @make_route("select")
# def func1():
#     print("select")
#
# @make_route("insert")
# def func2():
#     print("insert")
#
# @make_route("update")
# def func3():
#     print("update")
#
# @make_route("delete")
# def func4():
#     print("delete")
#
# print(route_dic)



#题目九
# import time
# import os
#
# def logger(logfile):
#     def deco(func):
#         if not os.path.exists(logfile):
#             with open(logfile,'w'):pass
#
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             with open(logfile,'a',encoding='utf-8') as f:
#                 f.write('%s %s run\n' %(time.strftime('%Y-%m-%d %X'),func.__name__))
#             return res
#         return wrapper
#     return deco
#
# @logger(logfile='aaaaaaaaaaaaaaaaaaaaa.log')
# def index():
#     print('index')
#
# index()

def logfile(logpath):
    def wrapper(func):
        def inner(*args,**kwargs):
            ret=func(*args,**kwargs)
            with open(logpath,"a",encoding="utf-8") as f:
                f.write("%s %s run \n" %(time.strftime("%Y-%m-%d %x"),func.__name__))
            return ret
        return inner
    return wrapper

@logfile(logpath="warpper.log")
def index():
    print("index")

index()

