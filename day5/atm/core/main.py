#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
main program handle module , handle all the user interaction stuff

'''
#导入时间time模块
#导入core包里的auth，accounts，logger，transaction，login_required模块
from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
import time

#transaction logger 定义交易日志的名字
trans_logger = logger.logger('transaction')
#access logger 定义访问日志的名字
access_logger = logger.logger('access')


#temp account data ,only saves the data in memory 记录用户的登录状态
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
#定义账户信息函数
def account_info(acc_data):
    print(user_data)
@login_required#调取登录函数
#定义还款函数
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])#重新加载账户最新数据
    #for k,v in account_data.items():
    #    print(k,v )
    #打印信用值和余额
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False #如果不回退，就一直循环
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()#输入还款金额
        if len(repay_amount) >0 and repay_amount.isdigit():#如果输入长度大于0，并且输入的是数字
            # print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:#打印新的余额
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
        else:#如果输入为空或者不是数字，返回无效的值
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)
        if repay_amount == 'b':#如果输入b则返回主菜单
            back_flag = True

#定义取款函数
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])#重新加载账户最新数据
    # 打印信用值和余额
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:#如果不回退，就一直循环
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()#输入取款金额
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():#如果输入长度大于0，并且输入的是数字
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:#打印新的余额
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
        else:#如果输入为空或者不是数字，返回无效的值
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
        if withdraw_amount == 'b':#如果输入b则返回主菜单
            back_flag = True

#定义转账函数
def transfer(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:#如果不回退，就一直循环
        transfer_amount = input("\033[33;1mInput transfer amount:\033[0m").strip()#输入取款金额
        if len(transfer_amount) > 0 and transfer_amount.isdigit():#如果输入长度大于0，并且输入的是数字
            new_balance = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
            if new_balance:#打印新的余额
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
        else:#如果输入为空或者不是数字，返回无效的值
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)
        if transfer_amount == 'b':
            back_flag = True
def pay_check(acc_data):
    pass
def logout(acc_data):
    pass
def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''#打印主菜单
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {#主菜单对应的字典
        '1': account_info,
        '2': repay,
        '3': withdraw, #取款
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()#用户选项
        if user_option in menu_dic:#如果用户选项在菜单里
            print('accdata',acc_data)
            #acc_data['is_authenticated'] =False
            menu_dic[user_option](acc_data)
        else:#如果用户选项不在菜单里则返回选项不存在
            print("\033[31;1mOption does not exist!\033[0m")
#定义运行函数
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data) #交互