import pickle,time,getpass,sys,smtplib
from prettytable import PrettyTable
from email.mime.text import MIMEText
from email.header import Header

def user():#初始化信息
	Userinfo = {}
	f = open('user.db','r',encoding="utf-8")
	for i in f.readlines():
		name,passwd,mail = i.split('|')
		Userinfo[name] = [passwd]
	return Userinfo
	f.close()
#Userinfo= user()
def login(card):
	count = 0
	while count < 3 :
		for i in open('lock.db',encoding="utf-8").readlines():
			if card in i:
				sys.exit('账号已锁定，请联系管理员')
		else:
			macth = 0
			passwd = getpass.getpass('输入你的密码:').strip()
			if len(passwd) != 0:
				if Userinfo[card][0] == passwd:
					print('%s,欢迎登陆' % card)
					macth = 1
					break
				else:
					macth == 0
					print ('passwd error')
					count += 1
			else:
				print('密码不能为空')
	else:	
		print('对不起,密码错误三次,账号已锁定')
		try:
			lock = pickle.load(open('lock.db','rb',encoding="utf-8"))
		except Exception:
			lock = [card]
			pickle.dump(lock,open("lock.db",'wb',encoding="utf-8"))
		else:
			lock.append(card)
			pickle.dump(lock,open("lock.db",'wb',encoding="utf-8"))
			sys.exit()
			
def menu(card):
	print ('''
			欢迎登陆渣打银行ATM系统
		1:取现							
		2:查询日志					
		3:还款              	 
		4:转账
		5:购物
		6:退出
		''')
	op = input('请输入你的选择:')
	return op
	
def getBal(card):#获取余额
	try:
		card_info = pickle.load(open('cardinfo','rb'))
	except Exception:
		card_info = {card: [float(15000)]}
		pickle.dump(card_info,open('cardinfo','wb'))
		return card_info[card][0]
	else:
		if card in card_info:
			return card_info[card][0]
		else:
			card_info[card] = [float(15000)]
			pickle.dump(card_info,open('cardinfo','wb'))
			return card_info[card][0]
def insertBal(card,num):#插入余额
	card_info = pickle.load(open('cardinfo','rb'))
	card_info[card] = [float(num)]
	pickle.dump(card_info,open('cardinfo','wb'))
	
def getlog(card,status,data,balance,description):#日志
	mg = [card,data,status,description,str(balance)]
	try:
		log_info = pickle.load(open('loginfo','rb'))
	except Exception:
		log_info = {card:[mg]}
		pickle.dump(log_info,open('loginfo','wb'))
	else:
		if card in log_info:
			log_info[card].append(mg)
			pickle.dump(log_info,open('loginfo','wb'))
		else:
			log_info[card] = [mg]
			pickle.dump(log_info,open('loginfo','wb'))
			
def showlog(card):#打印日志
	try:
		log_info = pickle.load(open('loginfo','rb'))
	except Exception:
		print ('not ')
	else:
		if card in log_info:
			x = PrettyTable(['card','datetime','status','log','balance'])
			for i in log_info[card]:
				x.add_row(i)
			print (x)
		else:
			money = getBal(card)
			print('您的总额为 %s' % money)
def transfer_accounts(card):#转账
	num = getBal(card)
	print('您的余额为 %s' %num)
	while True:
		account_num = input('请输入对方的账号:').strip()
		if len(account_num) != 0 and account_num in Userinfo and account_num != card:
			while True:
				money = input('请输入转账金额:').strip()
				my_bal = getBal(card)
				if len(money) != 0 and money.isdigit() and 0 < float(money) < float(my_bal):
					timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
					account_bal = getBal(account_num)
					account_bal += float(money)
					log = '%s 转款给你 %s' %(card,money)
					getlog(account_num,'转款',timenow,account_bal,log)
					insertBal(account_num,account_bal)
					
					my_bal -= float(money)
					insertBal(card,my_bal)
					log = '您给 %s 转款 %s' % (account_num,money)
					
					getlog(card,'转款',timenow,my_bal,log)
					print (log)
					break
				else:
					print('请输入正确的金额')
			break
		else:
			print('账号不存在.')
			continue	
def repayment(card):#还款
	mun = 15000 - getBal(card)
	print( '本期应还金额为%s' % mun)
	while True:
		money = INPUT_1
		if len(money) != 0 and money.isdigit() and  0 < float(money) < 15000:
			re_money = getBal(card) +float(money)
			insertBal(card,float(re_money))
			log = '还款：%s' % money
			print (log)
			timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			getlog(card,'还款',timenow,getBal(card),log)
			break
		else:
			print('请输入正确金额')
			continue
		
#transfer_accounts('zhaofei')
	
def cash(card):#取现
	bal = getBal(card)
	print('余额：%s' % bal)
	while True:
		money = input('输入金额:').strip()
		if len(money) != 0 and money.isdigit() and float(money) + float(money) * 0.005 < bal:
			num = bal - (float(money) + float(money) * 0.005)
			insertBal(card,num)
			log = '取款：%s ,利息：%s' % (money,float(money) * 0.005)
			print (log)
			timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			getlog(card,'取款',timenow,str(num),log)
			break
		else:
			print('输入错误，请重新输入')

def shopping(card):#购物
	num = getBal(card)
	print ('RMB：%s' % num)
	product_list = [
	('Iphone',5800),
	('Bike',800),
	('Book',45),
	('Coffee',35),
	('Solo 2 Beats',1590),
	('MX4',1999),
]	
	shopping_list = []
	while True:
		index = 1
		for item in product_list:
			# print ('\033[32;1m%s : %s\t%s\033[0m' % (index,item[0],item[1]))
			print(index,item[0],item[1])
			index += 1
		print('输入0退出购物系统')
		user_choice = input("请输入商品编号:").strip()
		if len(user_choice) != 0 and user_choice.isdigit():		
			if int(user_choice) == 0:
				break
			user_choice = int(user_choice)
			user_choice -= 1
			item_price = int(product_list[user_choice][1])
			money = getBal(card)
			timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			if money > item_price:
				log = '购物:%s' % item_price
				print (log)
				money -= item_price
				print ('余额：%s' %money)
				insertBal(card,float(money))
				getlog(card,'shopping',timenow,getBal(card),log)
			else:
				print('余额不足 %s' % getBal(card))
		else:
			print('输入错误,请重新输入')
# def card_mail(card):
	# print('未开通')
#shopping('zhaofei')		
def card_exit(card):#退出
	sys.exit('您已退出管理菜单')
def card_error(card):
	print('不存在，请重新输入:')

go = {
	'1':cash,
	'2':showlog,
	'3':repayment,
	'4':transfer_accounts,
	'5':shopping,
	# '6':card_mail,
	'6':card_exit}
if __name__ == '__main__':
	while True:
		Userinfo= user()
		card = input('输入你的帐号:')
		if len(card) != 0:
			if card in Userinfo.keys():
				login(card)
				while True:
					op = menu(card)
					go.get(op,card_error)(card)
			else:
				print('账号不存在')
		else:
			print('帐号不能为空')
			continue

















			
