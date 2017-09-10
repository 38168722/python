#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：Lyon
# 购物车
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998},
    ]
shopping_dict = {}
shopping_list = []
tag1 = True
while tag1:
    salary = input("请输入你的资产:").strip()
    if salary.isdigit():
        salary = int(salary)
    else:
        print("输入内容不得包含出数字外的其他字符！")
        continue
    while tag1:
        choose = input('''请输入操作号：\na.  购买商品\nb.  清空购物车\nc.  修改商品数量\nd.  查询余额\ne.  余额充值\nf.  退出商城并打印清单''')
        if choose == 'a':
            tag2 = True
            while tag2:
                print("商品信息如下".center(30,' '))
                for i, item in enumerate(goods, 1):
                    print("序号：{seq}\t\t名称：{name}\t\t价格：{price}".format(seq=i, name=item['name'], price=item['price']))
                goods_seq = input("请输入要购买的商品序号：").strip()
                if goods_seq.isdigit():
                    goods_seq = int(goods_seq)
                    if goods_seq>= 1 and goods_seq<= 4:
                        if goods_seq in shopping_list:
                            shopping_dict[goods_seq]['quantity'] += 1
                        else:
                            shopping_dict[goods_seq] = goods[goods_seq-1]
                            shopping_dict[goods_seq].setdefault('quantity', 1)
                        print("添加成功！")
                        tag2 = False
                    elif goods_seq <= 1 and goods_seq >= 4:
                        print("请输入1到4的数字序号！")
                else:
                    print("输入内容不得包含出数字外的其他字符！")
        elif choose == 'b':
            shopping_dict.clear()
            shopping_list.clear()
            print("已清空购物车！")
        elif choose == 'c':
            if len(shopping_dict) == 0:
                print("目前还没有商品哦，所以你没法改。")
                tag3 = False
            else:
                tag3 = True
            while tag3:
                print("已购商品如下".center(30, ' '))
                for i in shopping_dict.keys():
                    print("商品序号：{seq}\t\t商品名：{name}\t商品价格：{price}\t购买数量：{quantity}".format(seq=i, name=shopping_dict[i]['name'], price=shopping_dict[i]['price'], quantity=shopping_dict[i]['quantity']))
                while tag3:
                    edit = input("请输入要修改的商品序号：").strip()
                    if edit.isdigit():
                        edit = int(edit)
                        if edit in shopping_dict.keys():
                            while tag3:
                                quantity = input("请输入修改后的数量：").strip()
                                if quantity.isdigit():
                                    shopping_dict[edit]['quantity'] = quantity
                                    tag3 = False
                                    print("修改成功。")
                                else:
                                    print("输入内容不能包含出数字以外的字符。")
                        else:
                            print("输入序号不存在请重新输入。")
                    else:
                        print("输入内容不能包含出数字以外的字符。")
        elif choose == 'd':
            total_money = 0
            for i in shopping_dict.values():
                total_money += int(i['quantity']) * int(i['price'])
            if (salary - total_money) >= 0:
                print("你的余额为：%s" % (salary-total_money))
            else:
                print("你已经没有余额啦，请及时充值！")
        elif choose == 'e':
            tag4 = True
            while tag4:
                balance_recharge = input("请输入充值金额：").strip()
                if balance_recharge.isdigit():
                    balance_recharge = int(balance_recharge)
                    salary += balance_recharge
                    tag4 = False
                else:
                    print("输入内容不得包含出数字外的其他字符！")
        elif choose == 'f':
            if len(shopping_dict) == 0:
                print("穷光蛋，你什么也没买。")
            else:
                total_money = 0
                for i in shopping_dict.values():
                    total_money += int(i['quantity'])*int(i['price'])
                if (salary - total_money) >= 0:
                    print("你的剩余余额为%d"%(salary-total_money))
                    print("购物清单如下".center(30, ' '))
                    for i in shopping_dict.values():
                        print("商品名称：{name}\t商品价格：{price}\t购买数量：{quantity}".format(name=i['name'], price=i['price'], quantity=i['quantity']))
                else:
                    print("你的钱不够啦，放点东西回去吧。")
                    continue
            tag1 = False
        else:
            print("输入操作号有误，需要重新输入。")