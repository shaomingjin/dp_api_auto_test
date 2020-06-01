#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 0006 下午 16:28
# @Author : ShaoMingJin

import unittest,time
from util.operation_excel import OperationExcel
from data.get_data_fromexcel import GetDataFromExcel
from com.login import Login
from util.get_md5 import GetMD5
from util.logger import Logger
from util.read_config import ReadConfig
from util.verify_testresult import CheckPoint

'定义测试用例基类'
class BaseTestCase(unittest.TestCase):
    excel_path = ReadConfig.get_file_name("file_name")

    @classmethod
    def setUpClass(self) :
        # 初始化
        self.reponse = None
        self.check = CheckPoint()
        self.opera = OperationExcel(self.excel_path, 0)
        self.getdata = GetDataFromExcel(self.excel_path, 0)
        self.data_list = self.opera.data
        self.login = Login(self.excel_path, 0)
        self.get_md5 = GetMD5()
        # 调用登录方法
        Logger().info("开始调用公共的登录方法")
        self.response = self.login.login()
        self.uid = self.response.get("data").get("uid")
        self.key = self.response.get("data").get("key")
        self.gettime = self.get_md5.get_time()
        self.sign = self.get_md5.get_sign(self.uid + self.gettime)
        Logger().info("【登录成功后，获取到的uid为：{}，获取到的key为：{}.】".format(self.uid, self.key))


    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()



