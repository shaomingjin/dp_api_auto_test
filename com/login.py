#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/18 22:17 
# @Author : ShaoMingJin
from api.api_login_excel import ApiLogin
from util.read_config import ReadConfig
from util.operation_excel import OperationExcel


class Login(object):
    def __init__(self,file_name,sheet_id):
        self.opera = OperationExcel(file_name, sheet_id)
        #获取Excel表格中所有数据
        self.data_list = self.opera.data

    #公共方法，返回相应数据
    def login(self):
        for index in range(len(self.data_list)):
            api_name = self.data_list[index].get("接口名称")
            url = self.data_list[index].get("url")
            method = self.data_list[index].get("请求方式")
            header = self.data_list[index].get("请求头header")
            request_data = self.data_list[index].get("请求数据")
            prority = int(self.data_list[index].get("优先级"))
            if api_name == "login" and prority == 1:
                url_api = ReadConfig.get_host('url')+ url
                self.response = ApiLogin().api_post_login(url_api, method, header, request_data)
        return self.response