#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 15:17
# @Author  : Aries
# @Site    : 
# @File    : 类的封装.py
# @Software: PyCharm

# class Teacher:
#     __school="oldboy"
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#
#     def __foo(self):
#         print("sssss",self.__salary)
#
# t=Teacher('egon',3000)
# t._Teacher__foo()
# class Foo:
#     def __func(self):
#         print("from foo")
#
# class Bar(Foo):
#     def __func(self):
#         print("from Bar")
#
# b=Bar()
# b._Foo__func()
# b._Bar__func()

# class A:
#     def foo(self):
#         print("from A.foo")
#         # self.bar()
#         A.bar(self)
#     def bar(self):
#         print("from A.bar")
#
# class B(A):
#     def bar(self):
#         print("from B.bar")
#
# b=B()
# b.foo()

# class A:
#     def foo(self):
#         print("from A.foo")
#         self.__bar()
#     def __bar(self):
#         print("from A.bar")
#
# class B(A):
#     def __bar(self):
#         print('from B.bar')
#
# b=B()
# b.foo()
# class People:
#     def __init__(self,name,age,sex,height,weight,permission=False):
#         self.__name=name
#         self.__age=age
#         self.__sex=sex
#         self.__height=height
#         self.__weight=weight
#         self.permission=permission
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,val):
#         if not isinstance(val,str):
#             raise TypeError("名字必须是字符串")
#         self.__name=val
#     @name.deleter
#     def name(self):
#         if not self.permission:
#             raise PermissionError("不让删除")
#         del self.__name
#
#     @property
#     def tell_bmi(self):
#         res=self.__weight / (self.__height ** 2)
#         print('name:%s bmi:%s'%(self.__name,res))
#     def tell_info(self):
#         print('''
#         ------%s info
#         name:%s
#         age:%s
#         sex:%s
#         height:%s
#         weight:%s
#         '''%(self.__name,self.__name,self.__age,self.__sex,self.__height,self.__weight))
#
# egon=People("egon",18,"male",1.79,149)
# egon.name="alex"
# egon.permission=True
# print(egon.name)
# del egon.name
# print(egon.name)

# class Foo:
#     __x=1
#
# print(Foo._Foo__x)

#
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#     @property
#     def bmi(self):
#         return self.weight/(self.height ** 2)
# f=People("egon",70,1.80)
# f.height=1.82
# print(f.bmi)
# import hashlib
# class People:
#     def __init__(self,name):
#         self.name=name
#     def bar(self):
#         print("---->",self.name)
#     @classmethod
#     def func(self):
#         print(self)
#
#     def abc():
#         pass
#
#     def create_id(x,y):
#         m=hashlib.md5()
#         m.update()
#
# p=People("egon")
# # print(People.func)
# p.func()
# p.abc()

import hashlib
import time
class People:
    def __init__(self,name,sex,user_id):
        self.name=name
        self.sex=sex
        self.user_id=user_id
        self.id=self.create_id()
    def bar(self):
        print("--->",self.name)

    def create_id(self):
        m=hashlib.md5()
        m.update(self.name.encode("utf-8"))
        m.update(self.sex.encode("utf-8"))
        m.update(str(self.user_id).encode("utf-8"))
        return m.hexdigest()

f=People("egon","male",123321321)
print(f.id)