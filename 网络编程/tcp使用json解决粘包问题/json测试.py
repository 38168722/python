#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 14:12
# @Author  : Aries
# @Site    : 
# @File    : json测试.py
# @Software: PyCharm
import struct
import json
import pickle
header_dic={'total_size':232132132132132132132,
            'filename':None,
            'md5':None}
json_str=json.dumps(header_dic)
header=json_str.encode("utf-8")
print(len(header))