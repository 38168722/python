#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    def printInfo(self):
        print("年:",self.year,"月:",self.mon,"日:",self.day)


class Student:
    # def __init__(self,name,age,sex,year,mon,day):
    #     self.name=name
    #     self.age=age
    #     self.sex=sex
    #     self.birth=Date(year,mon,day)
    def __init__(self,name,age,sex,birthday):
        self.name=name
        self.age=age
        self.sex=sex
        self.birthday=birthday



    def talk(self):
        print("姓名%s 年龄%s 性别%s"%(self.name,self.age,self.sex))
        self.birthday.printInfo()


s1=Student("jack",31,"man",Date(2013,22,11))
s1.talk()