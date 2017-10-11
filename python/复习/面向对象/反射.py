#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Teacher:
    school="oldboy"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print("say people language")

    def __str__(self):
        return "<name:%s age:%s>"%(self.name,self.age)


class Foo:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def __delitem__(self, key):
        self.__dict__.pop(key)

    def __len__(self):
        return 10

f=Foo("egon",18,"male")

print(len(f))


