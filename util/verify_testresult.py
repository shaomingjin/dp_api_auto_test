#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 12:00
# @Author : ShaoMingJin

import unittest,json
from util.logger import Logger

class CheckPoint(unittest.TestCase):

    def __init__(self):
        self.logger=Logger()
        self.error=0

    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否在另外一个字符串中
        :param str_one:
        :param str_two:
        :return:
        '''
        if isinstance(str_one, dict):
            str_one = json.dumps(str_one)
        if isinstance(str_two, dict):
            str_two = json.dumps(str_two)
        '''
        str_one: 查找的字符串
        str_two:  被查找的字符串
        '''
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    # 字典是否相等方法
    def is_equal(self, test_result, expect_result):
        '''
        判断两个字典是否相等
        :param test_result:
        :param expect_result:
        :return:
        '''

        result = None
        flag=0
        if isinstance(test_result, str):
            dict_one = json.loads(test_result)
        if isinstance(expect_result, str):
            dict_two = json.loads(expect_result)
        try:
            self.assertDictEqual(test_result,expect_result)
            result=True
        except:
            result = False
            self.error+=1
        return result


    def result(self):
        if self.error>0:
            self.assertTrue(False)

