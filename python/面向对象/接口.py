#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Teacher:
    def __init__(self,name,age,sex,salary,permission=False):
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__salary=salary
        self.permission=permission


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        if not isinstance(val,str):
            raise TypeError("类型错误")
        self.__name=val

    @name.deleter
    def name(self):
        if not self.permission:
            raise PermissionError("不让删")
        del self.__name

    @property
    def getInfo(self):
        print("""
        display %s information
            name==%s
            age==%s
            sex==%s
            salary==%s
        """%(self.__name,self.__name,self.__age,self.__sex,self.__salary))


t1=Teacher("egon",33,"woman",3000)
print(t1.permission)
t1.permission=True
print(t1.name)
del t1.name
