#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/9 0009 上午 9:32 
# @Author : ShaoMingJin

import os
from configobj import ConfigObj
from util.logger import Logger
from util.get_projectpath import GetProjectPath

#新建读取配置文件类
class OperationConfig(object):

    #定义构造函数，返回文件路径
    def __init__(self,file_name):
        self.file_path=GetProjectPath().get_projectPath() + "config\\"+file_name

    '读取配置文件方法，返回一个字典'
    def readProperty(self,key):
        try:
            Logger().info("开始从{}文件中读取关键字：{}：".format(self.file_path,key))
            config = ConfigObj(self.file_path, encoding='UTF8')
            # 读配置文件
            dict =config[key]
            return dict
        except FileNotFoundError as e:
            Logger().error("读取配置文件失败.{}：".format(e))

if __name__ == '__main__':
    read =OperationConfig("config.ini")
    dict =read.readProperty('url')
    print(dict)
    print( dict.get('host'))


