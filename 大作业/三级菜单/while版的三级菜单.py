#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu={
    "北京":{
        "海淀":{
            "五道口":{
                "soho":{},
                "网易":{},
                "google":{}
            }
        },
        "昌平":{
            "沙河":{
                "老男孩":{},
                "北航":{},
                "南航":{}
            }
        }
    }
}
#
# for i in menu{"北京"}
#     print(i);

# while True:
#     choice = input(">>").strip();
#     if len(choice)==0 or choice not in menu:continue;
#     for i in menu[choice];
#         print(i);

# while True:
#     for key in menu:
#         print(key)
#     choice1=input("choice1>>:").strip()
#     if choice1=="b":break
#     if len(choice1)==0 or choice1 not in menu:continue
#     while True:
#         for key2 in menu[choice1]:
#             print(key2)
#         choice2=input("choice2>>:").strip()
#         if choice2=="b":break
#         if len(choice2)==0 or choice2 not in menu[choice1]:continue
#         for key3 in menu[choice1][choice2]:
#             print(key3)
#         choice3=input("choice3>>:").strip()
#         if choice3=="b":break
#         if len(choice3)==0 or choice3 not in menu[choice1][choice2]:continue
#         for key4 in menu[choice1][choice2][choice3]:
#             print(key4)
#         choice4= input("choice4>>:").strip()

# def getmenu(sdata):
#     while True:
#         for key in sdata:
#             print(key)
#         choice=input("choice:").strip()
#         if choice=="b":
#             break
#         if len(choice)==0 or choice not in sdata:continue
#         # for key2 in sdata[choice]:
#         #     print(key2)
#         getmenu(sdata[choice])
#
# getmenu(menu)
# level=[]
# # while True:
# #     for key in menu:
# #         print(key)
# #     choice = input("choice:>>")
# #     if choice=="b":
# #         if len(level)==0:
# #             break
# #         menu=level[-1]
# #         level.pop()
# #     if len(choice)==0 or choice not in menu:continue
# #     level.append(menu)
# #     menu=menu[choice]

test=[1,2,3,4,5]
print(test.pop())