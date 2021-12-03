import logging
import os
import time
from logging.handlers import RotatingFileHandler
from util import get_path



def get_log():
    #创建logger输出日志对象
    logger=logging.getLogger()
    #设置最低日志级别：debug、info、warning、error、critical
    logger.setLevel(level=logging.INFO)
    #获取项目根路径
    getpath = get_path.getPath()
    all_log_path1='result/logs/'
    #全部日志存放路径
    all_log_path=os.path.join(getpath,all_log_path1)
    ctime=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    #日志文件名称
    all_log_name=all_log_path+ctime+'.log'
    #所有日志：定义一个RotatingFileHandler，最多放3个日志文件，每个文件不超过1k
    all_handler=RotatingFileHandler(all_log_name,maxBytes=10*1024,backupCount=10)
    all_handler.setLevel(logging.INFO)

    #创建一个handler输出到控制台
    console_handler=logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    #设置输出日志格式:时间-日志器名称-日志级别-函数行-日志内容
    all_log_formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s")
    #给handler添加formatter
    all_handler.setFormatter(all_log_formatter)
    #给logger添加handler
    logger.addHandler(all_handler)
    return logger
logs=get_log()