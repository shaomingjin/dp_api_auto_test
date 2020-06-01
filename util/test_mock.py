#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:06 
# @Author : ShaoMingJin

#有mock实例

import requests
def requestr():
    r = requests.get("http://www.baidu.com") # 爬取百度网站的信息
    return r.status_code # 拿到status_code的状态码
print("无mock的实例返回的响应码为："+str(requestr())) # 200

import unittest
from unittest import mock
class TestClient(unittest.TestCase):  # 创建一个unittest类
    def test_success_request_01(self):  # 创建一条case
        self.assertEqual(requestr(), 200)  # 真实的接口断言;接口开发完,做断言,返回200表示正确
    # 接口未开发完,使用mock对象替换掉'r.status_code'的值
    def test_success_request_02(self):  # 创建一条预期与实际一致的正确case
        requestr = mock.Mock(return_value=200) # mock设为200
        self.assertEqual(requestr(), 200) # 预期与实际一致,通过
    def test_fail_request_01(self):  # 创建一条预期与实际一不致的case
        requestr = mock.Mock(return_value=404) # mock设为404
        self.assertEqual(requestr(), 200) # 实际结果是200,失败
    def test_fail_request_02(self):  # 创建一条预期与实际一致的错误case
        requestr = mock.Mock(return_value=404) # mock设为404
        self.assertEqual(requestr(),404) # 实际结果404 通过
if __name__ == '__main__':
    unittest.main()


