#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 8:36
# @Author  : Aries
# @Site    : 
# @File    : teacher.py
# @Software: PyCharm

class Teacher:
    def __init__(self,teacher_name,teacher_salary):
        self.teacher_name=teacher_name
        self.teacher_salary=teacher_salary
        self.teacher_class=[]   #班级列表
    def teacher_add_class(self,class_name,class_obj):
        self.teacher_class[class_name]=class_obj

