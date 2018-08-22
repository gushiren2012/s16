#!_*_coding:utf-8_*_
#__author__:"Alex Li"
#导入系统模块，导入日志模块
import os
import sys
import logging
#获取当前py文件的顶层绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
#定义数据库接口
DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

#定义日志级别
LOG_LEVEL = logging.INFO
#定义日志类型为交易日志和访问日志
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}
#定义交易日志的类型
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':-0.5},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}