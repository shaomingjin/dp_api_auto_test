#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 8:51 
# @Author : ShaoMingJin

import  os
import configparser
from config.get_file_path import GetFilePath
from util.logger import Logger

path=GetFilePath.get_path()
config_path=os.path.join(path,'config.ini') #路径拼接成配置文件的绝对路径
config=configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path,encoding='utf-8')

class ReadConfig():

    @classmethod
    def get_host(self,key):
        '''
        根据参数key获取相应host下的value
        :param key:
        :return:
        '''
        value=None
        try:
            value=config.get('HOST',key)
        except:
            Logger().error("获取-{}的值失败！！".format(key))
        return value

    @classmethod
    def get_email(self,key):
        value=None
        '''
        根据参数key获取相应email下的value
        :param key:
        :return:
        '''
        try:
            value=config.get('EMAIL',key)
        except:
            Logger().error("获取-{}的值失败！！".format(key))
        return value

    @classmethod
    def get_database_info(self,key):
        '''
        根据参数key获取相应database下的value
        :param key:
        :return:
        '''
        value=None
        try:
            value=config.get("DATABASE",key)
        except:
            Logger().error("获取-{}的值失败！！".format(key))
        return value

if __name__ == '__main__':
    print(ReadConfig.get_email('email_host'))
    print(ReadConfig.get_host('url'))


