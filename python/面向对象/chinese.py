#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 17:28
# @Author  : Aries
# @Site    : 
# @File    : chinese.py
# @Software: PyCharm

# from abc import ABCMeta,abstractclassmethod
#
# class Payment(metaclass=ABCMeta):
#     @abstractclassmethod
#     def pay(self,money):
#         pass
#
# class Alipay(Payment):
#
#     def pay(self,money):
#         print("支付宝付了%s元"%money)
#
# class Applepay(Payment):
#     def pay(self,money):
#         print("apple pay 支付了%s元"%money)
#
# def pay(payment,money):
#     payment.pay(money)
#
# p=Alipay()
# pay(p,200)

# from collections import namedtuple
# Course = namedtuple("course",['price','age',"hobby"]
# class Parent:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print("parent is func")
#
# class Son(Parent):
#     def func(self):
#         print("son is func")
#
# s=Son()

# class Parent:
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print("Parent func")
#
# class Son(Parent):
#     def __func(self):
#         print("son func")
#
# s = Son()
# print(Parent.__dict__)
# print(Son.__dict__)
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def area(self):
#         return pi*self.radius*self.radius
# from urllib.request import urlopen
# class Web_page:
#     def __init__(self,url):
#         self.url=url
#         self.__content=None
#
#     @property
#     def content(self):
#         if self.__content:
#             return self.__content
#         else:
#             self.__content=urlopen(self.url).read()
#             return self.__content
#
# mypage=Web_page('http://www.baidu.com')
# print(mypage)

class Foo:
    f="类的静态变量"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hi(self):
        print("hi,%s"%self.name)

obj=Foo('egon',73)
print(hasattr(obj,'name'))
print(hasattr(obj,'say_hi'))

n=getattr(obj,'name')
func=getattr(obj,'say_hi')
func()
print(getattr(obj,'aaaaaa','不在存啊!'))