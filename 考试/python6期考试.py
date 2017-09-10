#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/4 8:38
# @Author  : Aries
# @Site    : 
# @File    : python6期考试.py
# @Software: PyCharm
# 基础题
# 1.	执行python脚本的两种方式是？(1分)
'''
直接使用python执行或是使用pycharm运行
'''
#2.	python如何实现单行注释和多行注释（1分）
'''
单行注释 #  多行注释 ''' '''
'''
#3.	在python3中bytes类型与unicode类型二者之间如何相互转换？（1分）
'''
使用decode、encode 进行转换
'''
# 4.	创建一个对象有三个特性：身份id，类型，值
# 等号比较的是什么？（1分）
'''
等号比较的是内存地址是否相等
'''
# is比较的是什么？（1分）
'''
is 比较的是值与内存地址是否相等
'''
# 5.	使用链式赋值的方式将10赋值给变量x、y、z（1分）
'''
x,y,z=10
'''
# 6.	有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量（1分）
'''
名字 data[0]  年龄 data[1]  出生年data[2][0]  出生月 data[2][1]  出生日 data[2][2]
'''
# 7.	所有数据类型自带布尔值，布尔值为假的有？（1分）
'''
布尔值为假的有 0  NULL, "" NONE
'''
# 8.	常用数据类型有：字符串，列表，元组，字典，集合，请分类
# 按照存值个数分类？（1分）


# 按照可变\不可变类型分类？（1分）
'''
可变类型: 列表、字典、集合
不可变类型:字符串、元组
'''

# 按照取值方式分类（直接取值，按索引，按key取）？（1分）
'''
按索引取值的有: 元组、列表、字符串
按key取值的有: 字典
'''
# 按照有序\无序分类？（1分）
# 9.	阅读代码,请写出执行结果 （1分）
# a = "alex"
# b = a.capitalize()
# print(a)
# print(b)
'''
1 alex
2 Alex
'''
# 10.	阅读代码,请写出执行结果
# 代码一：（1分）
# if True or False and False:
#     print('yes')
# else:
#     print('no')
'''
结果为 yes
'''



# 代码二：（1分）
# if (True or False) and False:
#     print('yes')
# else:
#     print('no')
'''
执行结果为 no
'''

# 11.	写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
#   name = " aleX"
# 1)	移除 name 变量对应的值两边的空格,并输出处理结果
# name = " aleX".strip()
# print(name)   #aleX
# 2)	判断 name 变量对应的值是否以 "al" 开头,并输出结果
# name = " aleX"
# print(name.startswith("al"))  #False

# 3)	判断 name 变量对应的值是否以 "X" 结尾,并输出结果
# name = " aleX"
# print(name.endswith("X"))   #True

# 4)	将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# name = " aleX"
# print(name.strip().replace('l','p'))
# 5)	将 name 变量对应的值根据 “l” 分割,并输出结果。
# name = " aleX"
# print(name.split('l'))
# 6)	将 name 变量对应的值变大写,并输出结果
# name = " aleX"
# print(name.upper())
# 7)	将 name 变量对应的值变小写,并输出结果
# name = " aleX"
# print(name.lower())
# 8)	请输出 name 变量对应的值的第 2 个字符?
# name = " aleX"
# print(name[1])
# 9)	请输出 name 变量对应的值的前 3 个字符?
# name = " aleX"
# print(name[2])
# 10)	请输出 name 变量对应的值的后 2 个字符?
# name = " aleX"
# print(name[-2])

# 11)	请输出 name 变量对应的值中 “e” 所在索引位置?
# name = " aleX"
# print(name.index("e"))

# 12)	获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# print("oldboy"[0:-1])
# 12.	输出1-100内所有的奇数（1分）
# print([i for i in range(1,100) if i%2!=0])
# 13.	使用while循环输出1 2 3 4 5 6     8 9 10（1分）
# count=1
# while count<11:
#     if count==7:
#         count+=1
#         continue
#     print(count)
#     count+=1

# 14.	求1-2+3-4+5 ... 99的所有数的和（1分）
# sum=0
# for i in range(1,100):
#     if i%2==0:
#         sum=sum-i
#     else:
#         sum=sum+i
# print("和为",sum)

# 15.	编写for循环，利用索引遍历出每一个字符（1分）
# msg='hello egon 666'
# for i in msg:
#     print(i)
# 16.	编写while循环，利用索引遍历出每一个字符（1分）
# msg='hello egon 666'
# count=0
# while count<len(msg):
#     print(msg[count])
#     count+=1

# 17.	有变量msg='/etc/a.txt|365|get'（1分）
# 将该变量中的文件名，文件大小，操作方法切割出来
# msg='/etc/a.txt|365|get'
# fname=msg.split("|")
# print("文件名%s",fname[0],"文件大小",fname[1],"操作方法",fname[2])

# 18.	msg='hello alex'中的alex替换成SB（1分）
# msg='hello alex'
# msg=msg.replace("alex","SB")
# print(msg)
# 19.	编写while循环，让用户输入用户名和密码，如果用户为空或者数字，则重新输入（1分）
# while True:
#     name = input(">>please your name").strip()
#     password = input(">>please your password").strip()
#     if (not name) or (name.isdigit()): continue
#     print("login succefull!")

# 20.	有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。（2分）
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# jihe=[11,22,33,44,55,66,77,88,99,90]
# abc={"k1":[],"k2":[]}
# for i in jihe:
#     if i>=66:
#         abc["k1"].append(i)
#     else:
#         abc["k2"].append(i)
# print(abc)

# 21.	有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons={'alex','egon','yuanhao','wupeiqi','cobila','biubiu'}
# linuxs={'wupeiqi','oldboy','cobila'}
# 求出即报名python又报名linux课程的学员名字集合（2分）
# print(pythons&linuxs)
# 求出所有报名的学生名字集合（2分）
# print(pythons|linuxs)
# 求出只报名python课程的学员名字（2分）
# print(pythons-linuxs)
# 求出没有同时这两门课程的学员名字集合（2分）
# print(pythons^linuxs)

# 22.	统计s='hello alex alex say hello sb sb'中每个单词的个数（3分）
# 结果如下：
# {'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
# s='hello alex alex say hello sb sb'
# dic={}
# for i in s.split(" "):
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)

# 23.	简述什么是可迭代对象与迭代器对象？（2分）
#先有迭代器后才有迭代器对象，父子关系

# 判断下列数据类型是可迭代对象or迭代器（2分）
# from collections import Iterable
# from collections import Iterator
# 这个两分只能丢了，忘记判断方法了

# l=[1,2,3,4]
# print(isinstance(l,Iterator))
# t=(1,2,3)
# d={'a':1}
# set={1,2,3}
# f=open('a.txt')
#         分别用依赖索引和不依赖索引两种方式迭代上述对象（2分）
# 24.	文件a.txt内容：每一行内容分别为商品名字，价钱，个数
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 要求一：使用列表解析，从文件a.txt中取出每一行，做成下述格式（2分）
# [{‘name’:'apple','price':10,'count':3},{...},{...},...]
# car=[]
# with open("a.txt",encoding="utf-8") as fr:
#     for i in fr:
#         temp=i.strip().split(" ")
#         product={}
#         product["name"]=temp[0]
#         product["price"]=temp[1]
#         product["count"]=temp[2]
#         car.append(product)
# print(car)
# 要求二：求出总共消费了多少钱（5分）
# abc=list(map(lambda dic:int(dic["price"])*int(dic["count"]),car))
# print("共消费了",sum(abc))

# 25.	写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果，如{‘num’:3,’str’:2,’space’:3,’others’:3}（5分）

#
# def contstr(str1):
#     int numsum=0
#     int lettersum=0
#     int spacesum=0
#     int othersum=0
#     for i in str1:
#         if i.isdigit():
#             numsum+=1
#         elif i.isalpha():
#             lettersum+=1
#         elif i.isspace():
#             spacesum+=1
#         else:
#             othersum+=1
#         return {"num":numsum,"str":lettersum,"space":spacesum,"other":othersum}
# str1=input("请输入你要传入的字符串")
# contstr(str1)

# 3 综合题（40分）
# 1.	利用递归函数进行二分查找，查找下面列表中35的位置(10分)
# a)	l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#
# def find(source,aim,start,end):
#         mid=(start+end)//2
#         if source[mid]>aim:
#             end=mid-1
#             return find(source,aim,start,end)
#         if source[mid]<aim:
#             start=mid+1
#             return find(source,aim,start,end)
#         return mid
#
# print(find(l,35,0,len(l)))

# 2.	编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码（10分）
# 注意：从文件中读出字符串形式的字典，可以用eval
# user_state={
#     "user":None,
#     "status":False
# }
#
# def getUser():
#     with open("account",encoding="utf-8") as fr:
#         line=fr.readline().strip().split()
#         return {"user":line[0],"password":line[1]}
#
# userinfo = getUser()
#
# def checkUser():
#     while True:
#         user = input("please input your username:").strip()
#         password = input("please input your password:").strip()
#         if (not user) and (not password):continue
#         if user==userinfo["user"] and password==userinfo["password"]:
#             return True
#         break
#     return False
#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         if user_state["status"]:
#             ret = func(*args,**kwargs)
#         else:
#             if checkUser():
#                 user_state["user"]=userinfo["user"]
#                 user_state["status"]=True
#                 ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper
# def index():
#     print("welcome to home page")
#
# index()
# index()
# index()

# 3.	处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕（10分）
# def find(filename,content):
#     with open(filename,encoding="utf-8") as fr:
#         for i in fr:
#             if content in i:
#                 print(i)
#
# find("book","4")

# 4.	根据要求完成（10分）
# a)	现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
l1=('a','b')
l2=('c','d')
#我晕昨天学的忘记了,这么好赚分一个题就只能丢了。
# print({lambda x,y:zip(x,y),l1,l2})
print([{x:y}for x ,y in zip(l1,l2)])

# b)	用filter函数处理数字列表，将列表中所有的偶数筛选出来
# i.	num = [1,3,5,6,7,8]
# num = [1,3,5,6,7,8]
# print(list(filter(lambda x:x%2==0,num)))
















