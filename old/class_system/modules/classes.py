#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 8:35
# @Author  : Aries
# @Site    : 
# @File    : classes.py
# @Software: PyCharm

class Class:
    def __init__(self,class_name,course_obj):
        self.class_name=class_name
        self.class_course=course_obj
        self.class_student={}   #学生字典

