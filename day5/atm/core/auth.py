#!_*_coding:utf-8_*_
#__author__:"Alex Li"
#导入系统模块
import os
#导入core包的db_handler，logger函数模块，导入conf包的settings函数模块
from core import db_handler
from conf import settings
from core import logger
import json
import time
#定义登录函数
def login_required(func):
    "验证用户是否登录"
    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper
#定义登录认证函数
def acc_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    #连接数据库
    db_path = db_handler.db_handler(settings.DATABASE)
    #生成用户文件
    account_file = "%s/%s.json" %(db_path,account)
    print(account_file)
    #判断account_file是否文件
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:#打开读取
            account_data = json.load(f)#重新加载数据
            if account_data['password'] == password:#判断密码是否正确
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))#判断过期时间
                if time.time() >exp_time_stamp:#判断如果用户账户时间过期就返回过期信息提示换新卡
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else: #passed the authentication 如果没过期就返回账户数据
                    return  account_data
            else:#如果密码不正确则提示密码错误
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:#如果不是文件，则提示用户文件不存在
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)
#定义优化版认证接口函数
def acc_auth2(account,password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_api = db_handler.db_handler() # 获取数据库对象，执行sql语句并返回执行结果
    data = db_api("select * from accounts where account=%s" % account)#获取账户信息
    if data['password'] == password:#判断密码是否正确
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))#判断过期时间
        if time.time() > exp_time_stamp:#判断如果用户账户时间过期就返回过期信息提示换新卡
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else:  # passed the authentication，如果没过期就返回账户数据
            return data
    else:#如果密码不正确则提示密码错误
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")
#定义用户登录交互函数
def acc_login(user_data,log_obj):
    '''
    user authentcation
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0 #计数器为0
    while user_data['is_authenticated'] is not True and retry_count < 3 :#如果用户认证成功且登录次数小于三次
        account = input("\033[32;1maccount:\033[0m").strip()#输入账户名
        password = input("\033[32;1mpassword:\033[0m").strip()#输入密码
        user = acc_auth2(account, password)#调取acc_auth2优化版认证接口
        if user: #not None means passed the authentication
            user_data['is_authenticated'] = True#用户数据认证成功
            user_data['account_id'] = account#账户名正确
            # print("welcome")
            return user#返回用户查询信息
        retry_count +=1
    else:#返回登录次数太多并且记录到访问日志
        log_obj.error("account [%s] too many login attempts" % account)
        exit()#退出程序
