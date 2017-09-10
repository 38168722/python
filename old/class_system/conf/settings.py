#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 9:05
# @Author  : Aries
# @Site    : 
# @File    : settings.py.py
# @Software: PyCharm

import os
import sys
import platform

if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
    database_path = os.path.join(BASE_DIR,"database")

else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
    database_path = os.path.join(BASE_DIR, "database")

school_db_file = os.path.join(database_path,"school")