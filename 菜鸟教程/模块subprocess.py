#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 18:21
# @Author  : Aries
# @Site    : 
# @File    : 模块subprocess.py
# @Software: PyCharm
import subprocess
res=subprocess.Popen(cmd.decode("utf-8"),shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
stdout=res.stdout.read()
stderr=res.stderr.read()