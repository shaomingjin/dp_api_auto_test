#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/9 0009 上午 10:04 
# @Author : ShaoMingJin
#导包
import requests,json,ast
from urllib import parse
from util.logger import Logger
from util.run_method import RunMethod

#新建获取用户信息接口类
class ApiMyUserInfo(object):
    #新建获取用户信息方法
    def api_post_myuserinfo(self,api_url, api_method, header,request_data):
        #判断header是否为字符串
        if isinstance(header,str):
            header=json.loads(header)
        if isinstance(request_data,str):
            request_data=ast.literal_eval(request_data)
        #转换键值对格式，如：mobile=xxxxxx&password=xxxxx&.........
        request_data=parse.urlencode(request_data)
        Logger().info("个人中心接口请求数据为：{}." .format(request_data) )
        response=RunMethod().run_main(api_url,api_method,data=request_data,header=header)
        Logger().info("个人中心接口响应数据为：{}.".format(response))
        return response


