#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/8 0008 下午 18:23 
# @Author : ShaoMingJin
'''
目标：实现登录接口对象的封装
'''
#导包
import requests
import ast,json
from urllib import parse
from util.logger import Logger
from util.run_method import RunMethod

#新建类，登录接口对象
class ApiLogin(object):
    #新建方法，登录方法
    def api_post_login(self, api_url, api_method, header,request_data):
        #判断是否是字符串
        if isinstance(header,str):
            header=json.loads(header)
        if isinstance(request_data,str):
            #请求数据转为字典
            request_data=ast.literal_eval(request_data)
        #请求数据转键值对
        request_data=parse.urlencode(request_data)
        Logger().info("登录接口请求数据为：{}.".format(request_data))
        #调用post方法，并且返回服务器响应对象
        response=RunMethod().run_main(api_url, api_method, request_data,header)
        Logger().info("登录接口响应数据为：{}" .format(response))
        return response