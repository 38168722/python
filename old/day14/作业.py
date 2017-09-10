#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 16:34
# @Author  : Aries
# @Site    : 
# @File    : 作业.py
# @Software: PyCharm
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
#
# def auth_user():
#     with open("auth.txt","r",encoding="utf-8") as fr:
#         user_login=eval(fr.read())
#         name = input("name：")
#         pwd = input("password：")
#         if name == user_login["name"] and pwd in user_login["password"]:
#             return True
#         else:
#             return False
#
# user_state={"state":False}
#
# def check_login(func):
#     if not user_state["state"]:
#         auth_user()
#         user_state["state"]=True
#     def inner(*args,**kwargs):
#         print("执行前")
#         ret=func(*args,**kwargs)
#         print("执行后")
#         return ret
#     return inner
#
# @check_login
# def func1():
#     print("===功能模块一===")
#
# @check_login
# def func2():
#     print("===功能模块二===")
#
# @check_login
# def func3():
#     print("===功能模块三===")

# 保存指令，输入相关指令即可调用
# dic_func={"func1":func1,"func2":func2,"func3":func3}
# while True:
#     cmd = input("==>输入命令:")
#     if cmd not in dic_func:
#         print("无效的指令")
#         continue
#     dic_func[cmd]()



#1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# from urllib.request import urlopen
# def index(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# baidu=index("http://www.baidu.com")
# print(baidu())

#2、
#
# from urllib.request import urlopen
# import os
# cache_path=r'C:\Users\SKY\PycharmProjects\day14\cache.txt'
# def make_cache(func):
#     def wrapper(*args,**kwargs):
#         if os.path.getsize(cache_path):
#             #有缓存,文件不为空
#             print('\033[45m=========>有缓存\033[0m')
#             with open(cache_path,'rb') as f:
#                 res=f.read()
#         else:
#             res=func(*args,**kwargs) #下载
#             with open(cache_path,'wb') as f: #制作缓存
#                 f.write(res)
#         return res
#     return wrapper
# @make_cache
# def get(url):
#     return urlopen(url).read()
# print('================>first')
# print(get('https://www.qq.com'))
# print('================>second')
# print(get('https://www.python.org'))
# print('================>third')
# print(get('https://www.python.org'))



# import os
# from urllib.request import urlopen
# def make_cache(func1):
#     def inner(*args,**kwargs):
#         if(os.path.getsize("cache.txt")):
#             with open("auth.txt","r",encoding="utf-8") as fr:
#                 print("调用缓存")
#                 print(fr.read())
#         else:
#             with open("auth.txt","w",encoding="utf-8") as fw:
#                 res=func1(*args,**kwargs)
#                 print("重新下载")
#                 print(res)
#                 fw.write(res)
#                 return res
#     return inner
# @make_cache
# def geturl(url):
#     return urlopen(url).read()
#
# print(geturl("http://www.baidu.com"))
#
# from urllib.request import urlopen
# url_l=[]
# def mack_cache(func):
#     def inner(*args,**kwargs):
#         url=args[0]
#         filename=str(hash(url))
#         if url in url_l:
#             with open(filename,'r',encoding='utf-8') as fr:
#                 print("从缓存里读内容")
#                 ret=fr.read()
#         else:
#              url_l.append(url)
#              print("列表里存了什么",url_l)
#              ret=func(*args,**kwargs)
#              with open(filename,'w',encoding='utf-8') as fw:
#                 print("从网上下载的")
#                 fw.write(str(ret))
#         return ret
#     return inner
#
# @mack_cache
# def getUrl(url):
#     return urlopen(url).read()
#
# print(getUrl("http://www.baidu.com"))
# print(getUrl("http://www.baidu.com"))
# print(getUrl("http://www.baidu.com"))
# print(getUrl("http://www.baidu.com"))
#
from collections import Iterable,Iterator

str1="hello"
list1=[1,2]
tuple1=(1,2)
dic={'a':1}
set1={1,2,3}
f=open("a.txt",'w')
print(isinstance(str1,Iterator))
