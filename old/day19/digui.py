# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2017/8/2 15:04
# # @Author  : Aries
# # @Site    :
# # @File    : digui.py
# # @Software: PyCharm
#
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
# # def threeLM(dic):
# #     while True:
# #         for k in dic:print(k)
# #         key = input('input>>').strip()
# #         if key == 'b' or key == 'q':return key
# #         elif key in dic.keys() and dic[key]:
# #             ret = threeLM(dic[key])
# #             if ret == 'q': return 'q'
# #         elif (not dic.get(key)) or (not dic[key]) :
# #             continue
# #
# # threeLM(menu)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # s='hello'
# # print([i for i in s])
#
# abc=[1,31,73,84,57,22]
#
# print([i for i in abc if i>50])
#
# # def threeM(menu):
# #     for i in menu:
# #         print(i)
# #     n = input(">>>")
# #     if n in menu:
# #         for key in menu[n]:
# #             print(key)
# #         menu = menu[n]
# #         return threeM(menu)
# #
# # threeM(menu)
#
# import os
# f1=open('a.txt','r',encoding='utf-8')
# f2=open('temp.txt','w',encoding='utf-8')
#
# for line in f1:
#     f2.write(line.replace('python','hello'))
# f1.close()
# f2.close()
# os.remove('a.txt')
# os.rename('temp.txt','a.txt')
# import time
# import sys
# for i in range(0,101,2):
#     time.sleep(0.1)
#     char_num=i//2
#     per_str = '%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
#     print(per_str,end="",file=sys.stdout,flush=True)
# res = map(lambda x:x**2,[1,5,7,4,8])
# for i in res:
#     print(i)

# res = filter(lambda x:x>10,[5,8,11,9,15])
# for i in res:
#     print(i)

# dic={"name":"张三","age":44,"sex":"男"}
# res = filter(lambda x:x>10,[5,8,11,9,15])
# for i in res:
#     print(i)

# t1=('a','b')
# t2=('c','d')
# print([])

vec=[2,4,6]
max()