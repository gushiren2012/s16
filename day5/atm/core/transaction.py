#!_*_coding:utf-8_*_
#__author__:"Alex Li"
#导入core包的accounts，logger模块，导入conf包的settings模块
from conf import settings
from core import accounts
from core import logger
#transaction logger
#定义交易模块
def make_transaction(log_obj,account_data,tran_type,amount,**others):
    '''
    deal all the user transactions
    :param account_data: user account data
    :param tran_type: transaction type
    :param amount: transaction amount
    :param others: mainly for logging usage
    :return:
    '''
    amount = float(amount)
    if tran_type in  settings.TRANSACTION_TYPE:#如果交易类型符合原始交易类型
        interest =  amount * settings.TRANSACTION_TYPE[tran_type]['interest']#手续费=金额*利率
        old_balance = account_data['balance']#原始余额
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':#如果存钱
            new_balance = old_balance + amount + interest#新余额=原始余额+存入的钱+手续费
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':#如果取钱
            new_balance = old_balance - amount - interest#新余额=原始余额-取出的钱-手续费
            #check credit
            if  new_balance <0:#如果余额小于0，打印余额不足
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data) #save the new balance back to file，最新数据存到账户文件里
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %# 记录交易日志
                          (account_data['id'], tran_type, amount,interest) )
        return account_data#返回最新余额
    else:#如果不符合原始交易类型则提示交易类型不存在
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
