#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 9:03
# @Author  : Aries
# @Site    : 
# @File    : 日志模块.py
# @Software: PyCharm
# import logging
# logging.basicConfig(
#     level=logging.WARNING,
#     format="%(asctime)s---%(lineno)s---%(name)s:%(message)s",
#     filename="loging.txt",
#     filemode="a",
# )
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

import logging

log_obj=logging.getLogger()
fh=logging.FileHandler("log.txt")

ch=logging.StreamHandler()

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)
log_obj.addHandler(fh)
log_obj.addHandler(ch)
log_obj.setLevel(logging.ERROR)

log_obj.info("info")
log_obj.error("error")
log_obj.warning("warning")
log_obj.debug("debug")
log_obj.critical("cirtical")
