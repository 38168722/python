#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 19:23
# @Author  : Aries
# @Site    : 
# @File    : super类测试.py
# @Software: PyCharm
# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def prinInfo(self):
#         print("people类")
#
#
# class Teacher(People):
#     def __init__(self,name,age,sex,salary):
#         print("super是个啥",super())
#         print("super的类型",super().__dict__)
#         super().__init__(name,age,sex)
#         self.salary=salary
#
#     def prinInfo(self):
#         super().prinInfo()
#         print("teacher类")
#
# alex=Teacher("alex",33,"男",30000)
# alex.prinInfo()
#
# class Alive:
#     def __init__(self,sex):
#         self.sex=sex
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# class Student(Person):
#     def __init__(self,name,age,sex):
#        print(super())
#        super().__init__(name,age)
#        self.sex=sex
#
#
# s = Student("alex",23,"女")
# print(s.name)
# from urllib.request import urlopen
# class Web_pace:
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
# mypage=Web_pace("http://www.baidu.com")
# print(mypage.content)

# class Foo:
#     def __init__(self):
#         self.name="egon"
#         self.age=73
#     def func(self):
#         print(123)
#
# egg=Foo()
# if hasattr(egg,'func'):
#     Foo_func=getattr(egg,'func')
#     Foo_func()

# class Foo:
#     f=123
#     @classmethod
#     def class_method_demo(cls):
#         print("class_method_demo")
#
# print(hasattr(Foo,"class_method_demo"))
# method=getattr(Foo,"class_method_demo")
# delattr(Foo,"class_method_demo")
# print(hasattr(Foo,"class_method_demo"))

# class Foo:
#     def __init__(self,name):
#         self.name=name
#
#     # def __str__(self):
#     #     return "%s obj info in str"%self.name
#     #
#     def __repr__(self):
#         return "obj info in repr"
#
# f=Foo('egon')
# print("%s"%f)
# print("%r"%f)

# class Foo:
#     def __init__(self):
#         self.name="egon"
#         self.age=73
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# f=Foo()
# f["address"]="中国"
# print(f.__dict__)
# print(f["address"])
# del f["address"]
# print(f.__dict__)
# # print(f["address"])


