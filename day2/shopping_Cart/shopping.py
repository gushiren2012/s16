#!/usr/bin/env python
#-*- coding: utf-8 -*-
#by anthor zxy 2017-01-18
#blog:http://www.cnblogs.com/gushiren/
shopping_cart = []
salary = ["zhangxiaoyu",10000]
print(salary[1])
product_list_title = "\033[31m-----product list-----\033[0m"
welcome = "\033[32m-----------welcome to shopping marketi----------\033[0m"
product_list = [
    ("iphone 7",6500),
    ("ipod",3000),
    ("nokia",2000),
    ("civic",170000),
    ("CD",400),
    ("ThinaPad T420",5000),
]
print(welcome)
print(product_list_title)
for i in enumerate(product_list):
    index = i[0]
    p_name = i[1][0]
    p_price = i[1][1]
    print(index,":",p_name,p_price)
while True:
    choice = input("请输入要购买的商品编号>>>:     按q键退出").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice < len(product_list) and choice >= 0:
            p_item = product_list[choice]
            print(p_item)
            if p_item[1] <= salary[1]:
                shopping_cart.append(p_item)
                salary[1] -= p_item[1]
                print("购买的商品\033[32m:%s\033[0m已加入到购物车".center(40,'-')%(product_list[choice][0]))
                for item in  shopping_cart:
                    print(item)
                    print("您的余额为\033[31:1m%s\033[0m元" %salary[1])
            else:
                print("您的余额不足，差%s元"%(product_list[choice][1]-salary[1]))
        else:
            print("没有此件商品!")
	else:
        print("参数错误")		
    if choice == "q" or choice == "quit":
        cost = 0
        print("您购买的商品清单如下:")
        for i in shopping_cart:
            print(i)
            cost += i[1]
        print("消费总金额:",cost)
        print("您的余额为:",salary[1])
        break