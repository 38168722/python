#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 22:01
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm
#
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def walk(self):
#         print("%s is walking"%self.name)
#
#     def foo(self):
#         print("%s的名字是"%self.name)
#
# class Student(People):
#     def __init__(self,name,age,hobby):
#         People.__init__(self,name,age)
#         self.hobby=hobby
#
# class Teacher(People):
#     def __init__(self,name,age,salary):
#         People.__init__(self,name,age)
#         self.salary=salary
#     def foo(self):
#         People.foo(self)
#         print("from Teacher")
#
# s1=Student("egon",23,"play")
# t1=Teacher("alex",33,"shit")
# t1.foo()
class People:
    def __init__(self,name,age,year,mon,day):
        self.name=name
        self.age=age
        self.birthday=Date(year,mon,day)

    def walk(self):
        print("%s is walking"%self.name)

class Teacher(People):
    def __init__(self,name,age,year,mon,day,salary):
        People.__init__(self,name,age,year,mon,day)
        self.salary=salary
    def tech(self):
        print("%s is teaching"%self.name)

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
        print("出生于%s年%s月%s日"%(self.year,self.mon,self.day))

t=Teacher("egon",22,2017,10,1,10000)
t.tech()