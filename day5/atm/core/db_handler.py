#!_*_coding:utf-8_*_
#__author__:"Alex Li"
'''
handle all the database interactions
'''
#导入系统，时间，json模块
import json,time ,os
#导入conf包里的settings模块
from  conf import settings
#定义解析了db文件函数
def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    print('file db:',conn_params)
    #db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    return file_execute #返回函数file_execute的内存地址
#定义
def db_handler():
    '''
    connect to db
    :return:a
    '''
    conn_params = settings.DATABASE #获取数据库的配置
    if conn_params['engine'] == 'file_storage': #如果数据库引擎是file_storage
        return file_db_handle(conn_params)#调用文件处理的接口，传到file_db_handle
    elif conn_params['engine'] == 'mysql':#如果数据库引擎是mysql
        pass #todo  忽略什么都不做
#定义sql语句函数
def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE #获取数据库的配置
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])#获取数据库路径
    print(sql,db_path)
    sql_list = sql.split("where")#定义where判断条件
    print(sql_list)
    if sql_list[0].startswith("select") and len(sql_list)> 1:#如果sql语句是select开头且有where子语句
        column,val = sql_list[1].strip().split("=")
        if column == 'account':#如果条件与账户匹配
            account_file = "%s/%s.json" % (db_path, val)#生成账户文件
            print(account_file)
            if os.path.isfile(account_file):#判断账户文件是否是文件
                #f = open(account_file, 'r')
                with open(account_file, 'r') as f:#如果是文件则读取文件
                    account_data = json.load(f)#账户数据重新加载
                    return account_data#返回账户数据
                #f.close()
            else:#如果不是文件返回文件不存在
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val )
    elif sql_list[0].startswith("update") and len(sql_list)> 1:#如果sql语句是update开头且有where子语句
        column, val = sql_list[1].strip().split("=")
        if column == 'account':#如果条件与账户匹配
            account_file = "%s/%s.json" % (db_path, val)#生成账户文件
            #print(account_file)
            if os.path.isfile(account_file):#判断账户文件是否是文件
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:#如果是文件则读取文件
                    acc_data = json.dump(account_data, f)#刷新账户文件
                return True