#!/usr/bin/env python
#_*_coding:utf-8_*_
#by anthor zhangxiaoyu 2017-01-10
#blog:http://www.cnblogs.com/gushiren/
import sys
import getpass
import os
info = {'zhangxiaoyu':'123','zhangsan':'456','zhaosi':'789'}
count = 3
f = open('locked.txt','r')
lock_file = f.readlines()
f.close()
while True:
        username = raw_input("\033[32m请输入用户名:\033[0m").strip()
        password = getpass.getpass("\033[32m请输入密码:\033[0m").strip()
        for i in open('locked.txt').readlines():
                line=i.strip("\n")
                lock_file.append(line)
                if username in lock_file:
                        print("\033[41m用户%s已锁定，请联系系统管理员!\033[0m") % username
                        sys.exit()
        if username in info.keys():
                user_password = info['%s' %username]
                if password == user_password:
                        print "\033[36m登录成功！欢迎%s登录系统!\033[0m" % username
                        break
                else:
                        count -= 1
                        if count == 0:
                                f = open('locked.txt','a+')
                                f.writelines('%s'%username)
                                f.write('\n')
                                f.close()
                                print "\033[31m密码错误次数达到三次，该账户已锁定！\033[0m"
                                sys.exit()
                        else:
                                print "\033[33m密码错误,还剩%s次机会,超出次数账号将被锁定！\033[0m" % count
        else:
                print "\033[31m用户%s不存在,请重新输入:\033[0m" % username
                continue