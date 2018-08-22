#!/usr/bin/env python
#-*- coding: utf-8 -*-
#by anthor zxy 2017-01-18
#blog:http://www.cnblogs.com/gushiren/
zone = {
    '北京': {
        '海淀': ['五道口','北宫门','西三旗'],
        '朝阳': ['四惠','望京','来广营'],
        '昌平': ['立水桥','霍营','沙河'],
        '顺义': ['南法信','石门','牛栏山'],
        '通州': ['九棵树','台湖','潞河']
    },
    '河南': {
        '郑州': ['荥阳','新密','中牟'],
        '开封': ['杞县','兰考','尉氏'],
        '洛阳': ['偃师','孟津','伊川'],
        '南阳': ['邓州','南召','桐柏'],
        '信阳': ['固始','潢川','淮滨']
    },
    '浙江': {
        '杭州': ['拱墅','西湖','余杭'],
        '宁波': ['镇海','宁海','奉化'],
        '绍兴': ['新昌','上虞','诸暨'],
        '温州': ['鹿城','永嘉','乐清'],
        '台州': ['椒江','天台','仙居']
    },
    '江苏': {
        '南京': ['玄武','鼓楼','建邺'],
        '镇江': ['京口','润州','丹徒'],
        '扬州': ['广陵','高邮','邗江'],
        '苏州': ['金阊','沧浪','虎丘'],
        '宿迁': ['宿豫','沭阳','泗阳']
    }
}
pro_list = list(zone.keys())
print("\033[32m-------------------------------------------------\033[0m")
print ("+   \033[31m欢迎使用地区查询系统\033[0m   +")
print("\033[32m-------------------------------------------------\033[0m")
while True:
    print("省份".center(50,'+'))
    for i in pro_list:
        print(pro_list.index(i)+1,i)
    pro_id = input("请输入省份编号,或输入q(quit)退出:")
    if pro_id.isdigit():
        pro_id = int(pro_id)
        if pro_id > 0 and pro_id <= len(pro_list):
            pro_name = pro_list[pro_id-1]
            city_list = list(zone[pro_name].keys())
            while True:
                print("城市".center(50, '+'))
                for v in city_list:
                    print(city_list.index(v) + 1,v)
                city_id = input("请输入城市编号,或输入b返回上级菜单，或输入q退出:")
                if city_id.isdigit():
                    city_id = int(city_id)
                    if city_id > 0 and city_id <= len(city_list):
                        city_name = city_list[city_id-1]
                        town_list = zone[pro_name][city_name]
                        while True:
                            print("县".center(50, '+'))
                            for k in town_list:
                                print(town_list.index(k) + 1,k)
                            back_or_quit = input("输入b返回上级菜单,或输入q退出:")
                            if back_or_quit == "b":
                                break
                            elif back_or_quit == "q":
                                exit()
                            else:
                                print("已经到最后一层了，将直接返回城市列表！")
                                break
                    else:
                        print("编号为%s的城市编号不存在"%city_id)
                elif city_id == "b":
                    break
                elif city_id == "q":
                    exit()
                else:
                    print("参数错误")
        else:
            print("编号为%d的省份不存在" % pro_id)
    elif pro_id == 'q':
        break
    else:
        print("参数错误")







