#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 14:26
# @Author  : Aries
# @Site    : 
# @File    : 复习.py
# @Software: PyCharm

class People:
    country="china"
    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError("must be str")
        self.name=name
    def talk(self):
        print("====>")

class Teacher(People):
    def eat(self):
        print("%s is eating"%self.name)

    def talk(self):
        People.talk(self)
        print("Teacher%s say hello"%self.name)

t=Teacher("egon")
print(Teacher.mro())