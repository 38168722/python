#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Teacher:
    def __init__(self,name,age,education):
        self.name=name
        self.age=age
        self.education=education


class Student:
    school="欧得博爱"
    def __init__(self,name,age):
        self.name=name
        self.age=age

print(Student.__dict__["school"])
print(Student.__bases__)