#!/usr/bin/env python
#coding:utf-8
import getpass,smtplib,sys,pickle
from email.mime.text import MIMEText
userinfo = 'user.db'
def menu():
	'''主菜单'''
	print('''
			管理员专用
	1:创建账户				
	2:解锁账户
	3:退出系统	
	''')
	op = input('输入你的选择:')
	return op
#创建账号，密码，邮箱。
def card_num():
	while True:
		name = input('请输入你的用户名:').strip()
		if  len(name) < 4:
			print('帐号最少4位')
			continue	
		with open('user.db') as f:
			for i in f.readlines():
				num = i.strip().split('|')
				if name in num[0]:
					print('该账号已被注册,请重新输入')
					break
			else:
				while True:
					passwd1 = getpass.getpass().strip()
					passwd = getpass.getpass().strip()
					if len(passwd1) < 4 :
						print('密码最少4位')
						continue
					if passwd1 == passwd:
						mail = input('输入你的邮箱地址').strip()
						tmp = []
						tmp.append(name)
						tmp.append(passwd)
						tmp.append(mail)
						with open('user.db','a+') as f:
							f1 = '|'.join(tmp)
							f.writelines(f1+'\n')
						break	
					else:
						print('两次输入密码不同，请重新输入')
						continue					

				print('你的账号%s,以创建成功.'% name)
				break
def card_unlock():
	username = {}
	with open('user.db') as f:
		for i in f.readlines():
			name,passwd,mail = i.split('|')
			username[name] = [passwd]
		print(username.keys())
		while True:
			user = input('输入你要解锁的用户名:').strip()
			if user in username.keys():
				lock = pickle.load(open('lock.db','rb'))
				if user in lock:
					lock.remove(user)
					pickle.dump(lock,open('lock.db','wb'))
					print('帐号已解锁')
					break
				else:
					print('帐号未锁定')
					break
			else:
				print('账号不存在')
				continue

def card_exit():
	sys.exit('您已退出管理菜单')
def card_error():
	print('不存在，请重新输入:')
	
go  = {
	'1':card_num,
	'2':card_unlock,
	'3':card_exit
}
def main():
	while True:
		op = menu()
		go.get(op,card_error)()
if __name__ == '__main__':	
	main()

