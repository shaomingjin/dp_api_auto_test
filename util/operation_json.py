#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/16 14:33 
# @Author : ShaoMingJin

import json
from util.get_projectpath import GetProjectPath

class OperationJson(object):

    def __init__(self,file_name):
        #json文件路径
        self.file_path=GetProjectPath().get_projectPath()+"data\\"+file_name
        self.data=self.read_data()

    #读取json文件方法
    def read_data(self):
        #打开json文件
        with open(self.file_path,"r",encoding="utf-8") as fp:
            #调用load方法加载文件流，并返回数据
            data=json.load(fp)
            return data

    #根据关键字获取value
    def get_data_key(self,key):
        value=self.data.get(key)
        return value

    # 将cookies数据写入json文件
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))

    # 读取测试数据方法
    def get_data(self,key):
        datas = self.get_data_key(key)
        # 新建空列表，添加读取json数据s
        arrs = []
        # 遍历json文件
        for data in datas:
            arrs.append((data.get("id"),
            data.get("case_id"),
            data.get("case_name"),
            data.get("api_name"),
            data.get("api_method"),
            data.get("header"),
            data.get("api_url"),
            data.get("request_data"),
            data.get("expect_result"),
            data.get("priority")))
        return arrs

if __name__ == '__main__':
    opera=OperationJson("login.json")
    print(opera.get_data_key("login"))