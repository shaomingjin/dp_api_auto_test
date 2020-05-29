#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/16 1:08 
# @Author : ShaoMingJin

class global_var():
    #case_id
    Id = '0'
    api_name='1'
    case_name = '2'
    url = '3'
    run = '4'
    request_way = '5'
    request_header = '6'
    request_data = '7'
    expect = '8'
    result = '9'
    prority='10'
    run_time='11'

#获取caseid
def get_id():
    return global_var.Id
#获取api名称
def get_api_name():
    return global_var.api_name

#获取用例name
def get_case_name():
    return global_var.case_name

#获取url
def get_url():
    return global_var.url

#获取run
def get_run():
    return global_var.run

#获取request_way
def get_request_way():
    return global_var.request_way

#获取request_header
def get_header():
    return global_var.request_header

#获取请求数据data
def get_request_data():
    return global_var.request_data

#获取except
def get_expect():
    return global_var.expect

#获取result
def get_result():
    return global_var.result

#获取用例优先级
def get_prority():
    return global_var.prority

#获取用例执行时间
def get_run_time():
    return global_var.run_time

