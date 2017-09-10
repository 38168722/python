#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 15:20
# @Author  : Aries
# @Site    : 
# @File    : 函数作业.py
# @Software: PyCharm

# 基础作业：
# 1、整理今天的知识点、继续整合思维导图
# 2、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
#
# def update(fileName,old_content,new_content):
#     import os,sys
#     try:
#         with open(fileName,"r+",encoding="utf-8") as fr,open(fileName+".swap","w",encoding="utf-8") as fw:
#             for i in fr:
#                 fw.write(i.replace(old_content,new_content))
#         os.remove(fileName)
#         os.rename(fileName+".swap",fileName)
#         print("file update success")
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         print("file update failed")
#
# update("update1.txt","戴高乐","小布什")

# 3、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。

# def checkStr(content):
#    for i in range(len(content)):
#        if content[i].isspace():
#            print(content,"第%s个元素有空格"%{i})
#            break
#        else:
#            print("第%s个没有空格"%{i})
#
# checkStr(("hello"," "))

# 4、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def checkLength(name):
#     all=[]
#     for i in dic:
#         if len(dic[i])>2:
#             all.append({i:dic[i][0:2]})
#     return all
#
# print(checkLength(dic))


# 进阶作业(选做)：
# 用函数实现购物车程序

# def buy():
#     buy_car=[]
#     while True:
#      msg_dic = {
#         'apple': 10,
#         'tesla': 100000,
#         'mac':   3000,
#         'lenovo': 30000,
#         'chicken': 10,
#      }
#      for i in msg_dic:
#          print(i,msg_dic[i])
#      name = input("请输入你要购买的商品名")
#      if len(name)==0 and name not in msg_dic:continue
#      buy_car.append([name,msg_dic[name]])
#      print("您已购买的商品有:")
#      for i in buy_car:
#          print(i)
#      answer = input("是否继续Y/N")
#      if len(answer)==0 or answer not in ["y","n"]:continue
#      if answer=="n":
#          print("欢迎您的再次光临，再见")
#          break
# buy()

#
# 默写作业：
# 1.默写代码并且把print的结果说出来
# x = 1
# def f(x):
#     print(x)
# f(10)
# print(x)
#
# 2.默写代码并标清楚代码执行的步骤
# def f1():
#     a = 1
#     def f2():
#         def f3():
#             print(a)
#         f3()
#     f2()
# f1()
#
# 3.默写代码并标清楚代码执行的步骤／以及执行结果
# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     return inner
# f = func()
# f()
#
# 预习作业：
# 装饰器的博客 http://www.cnblogs.com/Eva-J/articles/7194277.html

# import time
# def timer(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         ret=func(*args,**kwargs)
#         print("共运行%s秒"%(time.time()-start))
#         return ret
#     return inner
#
# @timer
# def funny(x,y):
#     time.sleep(0.1)
#     print("x等于%s,y等于%s"%(x,y))
#
# funny("hello","world")
#
# flag=True
# def outer(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print("执行之前要做的事")
#              ret=func(*args,**kwargs)
#             if flag:
#                 print("执行之后要做的事")
#             return ret
#         return inner
#     return wrapper
#
# @outer(flag)
# def index():
#     print("===welcome to my home====")
#
# index()
import sys
# sys.setrecursionlimit(1000000)
# count=0
# def say():
#     # print("从前有个大和尚和小和尚")
#     global count
#     count+=1
#     print(count)
#     say()
#
# say()

# def age(n):
#     if n == 1:
#         return 40
#     else:
#         ret = age(n-1)
#         return ret + 2
#
# alex_age=age(5)
# print(alex_age)

# l=[1,2,3,4,5,6,7,8,9,10,11]
# def find(l,aim):
#     mid=len(l)//2
#     if l[mid]>aim:
#         new_l=l[:mid]
#         return find(new_l,aim)
#     elif l[mid]<aim:
#         new_l=l[mid+1:]
#         return find(new_l,aim)
#     else:
#         return l[mid]
#
# print(find(l,7))

# def add(a):
#     if a==1:
#         return a
#     else:
#         return a+add(a-1)
#
# print(add(100))

# def cal(num):
#     if num % 2 ==0:
#         num = num //2
#         return cal(num)
#     else:
#         return num
#
# print(cal(100))

# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
#
# def threeLM(menu):
#     for i in menu:
#         print(i)
#     n=input(">>>")
#     if n in menu:
#         for key in menu[n]:
#             print(key)
#         menu=menu[n]
#         return threeLM(menu)
#
# threeLM(menu)

# def age(n):
#     if n == 1:
#         return 40
#     else:
#         return age(n-1)+2
#
# print(age(4))
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#
# def func(l,aim):
#     mid=(len(l)-1)//2
#     if(aim>l[mid]):
#         func(l[mid+1:],aim)
#     elif(aim<l[mid]):
#         func(l[:mid],aim)
#     elif aim==l[mid]:
#         print("bingo",mid)
#
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
#
# def threeLM(menu):
#     for key in menu:
#         print(key)
#     k = input(">>>")
#     if k in menu:
#         threeLM(menu[k])
#
# threeLM(menu)
# l=[11,22,33,44,55,66,77,88,99]
# def find(l,aim):
#     mid = len(l)//2
#     if l[mid]>aim:
#         new_l=l[:mid]
#         return find(new_l,aim)
#     elif l[mid]<aim:
#         new_l=l[mid+1:]
#         return find(new_l,aim)
#     else:
#         return l[mid]
# print(find(l,66))

# def div(n):
#     if n%2!=0:
#         return n
#     print(n,"===")
#     n=n//2
#     return div(n)
#
# print(div(88))
# l=[11,22,33,44,55,66,77,88,99]
#
# def find2(l,aim,start,end):
#     if start<end:
#         mid=(start+end)//2
#         if(aim>l[mid]):
#             start=mid+1
#             return find2(l,aim,start,end)
#         if(aim<l[mid]):
#             end=mid-1
#             return find2(l,aim,start,end)
#         else:
#             return mid
#     else:
#         return "不存在"
# print(find2(l,100,0,len(l)))

# def threeLM(dic):
#     while True:
#         for k in dic:print(k)
#         key = input("input>>").strip()
#         if key =='b' or key=='q':return key
#         elif key in dic.keys() and dic[key]:
#             ret = threeLM(dic[key])
#             if ret == 'q':return 'q'
#         elif (not dic.get(key)) or (not dic[key]):
#             continue
# threeLM(menu)
#
# def f(x):
#     return x*100
# print(map(f,[1,2,3,4]))

# def add100(x):
#     return x+100
# list1=[11,22,33]
# print(list(map(add100,list1)))

# L = [1,2,3,4]
# def pow2(x):
#     return x*x
# print(list(map(pow2,L)))

# def is_odd(x):
#     return x%2==1
# print(list(filter(is_odd,[1,4,6,7,9,12,17])))
# print(list(map(is_odd,[1,4,6,7,9,12,17])))
# abc="hello world"

def tail(filename):
    f = open()
