#!_*_coding:utf-8_*_
#__author__:"Alex Li"
# 导入系统模块
import os   #
import sys
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#获取当前py文件的顶层绝对路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
#将返回的绝对路径加入到系统变量
sys.path.append(base_dir)

#导入core包下的main模块
from core import main
if __name__ == '__main__':
    main.run()#调取main模块里的run函数，并运行
