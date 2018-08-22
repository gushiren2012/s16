#!_*_coding:utf-8_*_
#__author__:"Alex Li"
#导入时间模块和json模块
import json
import time
#导入core包下的db_handler和settings模块
from core import db_handler
from conf import settings
#定义获取余额函数
def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_id)
    # 连接数据库
    db_api = db_handler.db_handler()
    #依照条件查询获取用户的数据
    data = db_api("select * from accounts where account=%s" % account_id)
    #返回用户数据
    return data
    # with open(account_file) as f:
    #     acc_data = json.load(f)
    #     return  acc_data
#定义更新用户数据函数
def dump_account(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''
    # 连接数据库
    db_api = db_handler.db_handler()
    # 依照条件更新用户的数据
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)
    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_data['id'])
    # with open(account_file, 'w') as f:
    #     acc_data = json.dump(account_data,f)
    return True