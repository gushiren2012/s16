#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
handle all the logging works
'''

import logging
from conf import settings
#定义日志函数
def logger(log_type):
    #create logger
    logger = logging.getLogger(log_type)#定义日志类型
    logger.setLevel(settings.LOG_LEVEL)#定义日志级别

    # create console handler and set level to debug
    ch = logging.StreamHandler()#
    ch.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to warning，创建文件处理程序并设置报警级别
    log_file = "%s/log/%s" %(settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # create formatter,定义日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh，格式化输入日志
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger，定义日志记录器
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
    # 'application' code 定义日志各种报警级别输出的内容
    '''logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')'''

