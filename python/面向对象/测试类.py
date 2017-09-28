#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 15:19
# @Author  : Aries
# @Site    : 
# @File    : 测试类.py
# @Software: PyCharm
class Course:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

    def tell_info(self):
        print('''
        ----------%s的课程信息---------
        课程名称:%s
        课程价格:%s
        课程周期:%s
        '''%(self.name,self.name,self.price,self.period))

class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


class Teacher(Person):
    def __init__(self,name,age,sex,salary):
        Person.__init__(self,name,age,sex)
        self.salary=salary
        self.course=[]

    def tell_course(self):
        for i in self.course:
            i.tell_info()



class Student(Person):
    def __init__(self,name,age,sex,grade):
        Person.__init__(self,name,age,sex)
        self.grade=grade




alex=Teacher("alex",33,"男",300000)
python=Course("python",30000,6)
php=Course("php",33333,5)
linux=Course("linux",50000,6)
alex.course.append(python)
alex.course.append(php)
alex.course.append(linux)
alex.tell_course()

