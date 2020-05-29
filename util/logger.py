#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 0008 下午 18:51
# @Author : ShaoMingJin

import logging,time,os
from util.get_projectpath import  GetProjectPath

#新建日志类
class Logger(object):
    #构造函数初始化
    def __init__(self):
        # 日志保存本地的路径
        self.log_path = GetProjectPath().get_projectPath() + "logs\\"
        # 文件的命名
        self.logname = os.path.join(self.log_path, '%s.log'%time.strftime('test_%Y%m%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  # logger等级总开关

        # 定义log的输出格式
        self.formatter = logging.Formatter(
            '[ %(asctime)s ]--%(threadName)-10s %(thread)d  line:%(lineno)d  [%(levelname)s] *** '
            '%(message)s',
            '%Y-%m-%d')

    def __console(self, level, message):
        '''
        创建一个FileHandler，用于写到本地
        :param level:
        :param message:
        :return:
        '''
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def start_case(self, case_id,case_name):
        self.info("**************************************第{}条测试用例，测试用例名称为：{}:开始执行**************************************".format(
            case_id,case_name))

    def end_case(self, case_id,case_name):
        self.info(
            "**************************************第{}条测试用例，测试用例名称为：{}:执行结束*************************************".format(case_id,case_name))