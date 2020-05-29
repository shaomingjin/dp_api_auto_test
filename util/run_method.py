#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 14:18
# @Author : ShaoMingJin

import requests
from util.logger import Logger

#发送请求基类的封装
class RunMethod(object):

    def __init__(self):
        #定义响应对象为空
        self.res=None

    def send_post(self,url,data,header=None):
        '''
        post 方法发送请求,并返回响应对象
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if header!=None:
            self.res=requests.post(url=url,data=data,headers=header).json()
        else:
            self.res=requests.post(url=url,data=data).json()
        return self.res

    def send_get(self,url,data,header=None):
        '''
        get方法发送请求，并返回响应对象
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if header!=None:
            self.res=requests.get(url=url,data=data,headers=header,verify=False).json() #verify=False  不信任的SSL证书忽略
        else:
            self.res=requests.get(url=url,data=data,verify=False).json()
        return self.res

    def run_main(self,url,method,data=None,header=None):
        '''
        主要调用该方法，进行post或get请求
        :param url:
        :param method:
        :param data:
        :param header:
        :return:
        '''
        #根据传入method判断接口的请求方法
        if method=="POST" or method=="post":
            self.res=self.send_post(url,data,header)
        elif method=="GET" or method=="get":
            self.res=self.send_get(url,data,header)
        elif method=="PUT" or method=="put":
             pass
        elif method=="DELETE" or method=="delete":
             pass
        else:
            Logger().info("请求方法错误！请求方法为：{}".format(method))
        return self.res

if __name__ == '__main__':
    url="https://app.service.yihuayidong.com/index/login"
    header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data="mobile=13700000123&password=111111q&type=0&gear=pc"
    run=RunMethod()

    print(run.send_post(url,data,header))