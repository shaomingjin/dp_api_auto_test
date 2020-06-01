#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 19:30
# @Author : ShaoMingJin

import ast,ddt
import unittest
from util.verify_testresult import CheckPoint
from util.read_config import ReadConfig
from util.operation_excel import OperationExcel
from util.logger import Logger
from util.get_current_time import GetCurrentTime
from api.api_myUserInfo import ApiMyUserInfo
from case.base_testcase import BaseTestCase

@ddt.ddt
class TestMyUserInfo(BaseTestCase):

    #获取个人中心测试用例
    @ddt.data(*OperationExcel(BaseTestCase.excel_path, 0).get_data_by_api_name("myUserallinfo"))
    def test_myUserInfo(self,data):

        case_id, api_name, case_name, url, is_run, request_method, header, request_data, expect, result, prority,run_time = tuple(
            data)
        # 判断测试用例是否运行
        if is_run == "yes":
            Logger().start_case(int(case_id), case_name)
            url=ReadConfig.get_host("url")+url
            #将字符串转为字典
            request_data=ast.literal_eval(request_data)
            if int(prority)==1:
                request_data["uid"]=self.uid
            request_data["gettime"]=self.gettime
            request_data["sign"]=self.sign
            request_data["u"]=self.uid
            request_data["key"]=self.key
            Logger().info("【开始调用个人中心接口,request_url:{},request_method:{},header:{},request_data:{}】".format(url,request_method,header,request_data))
            # 调用接口请求方法
            self.response = ApiMyUserInfo().api_post_myuserinfo(url, request_method, header, request_data)
            if self.response.get("data")!=""  or self.response.get("data")!='':
                # 定义空字典
                check_point = {}
                # 获取code,mobile和msg
                code = self.response.get("code")
                msg = self.response.get("msg")
                mobile = self.response.get("data").get("mobile")
                # 把code,msg和mobile添加到字典中
                check_point["code"] = code
                check_point["msg"] = msg
                check_point["mobile"] = mobile
                '''判断响应数据和期望结果是否一致'''
                if CheckPoint().is_equal(check_point, ast.literal_eval(expect)):
                    Logger().info(
                        "第{}条用例名称为：{}--执行成功，结果返回值为：{}，期望结果为：".format(int(case_id), case_name, self.response, expect))
                    # 把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id),"Pass",GetCurrentTime().get_curr_time())
                else:
                    Logger().error(
                         "【第{}条用例名称为：{}--执行失败！！，结果返回值为：{}，期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把错误的测试用例的响应数据回写到相应的实际结果中
                    self.getdata.update_excel(int(case_id),str(self.response),GetCurrentTime().get_curr_time())
                    self.check.result()
            else:
                if CheckPoint().is_equal(self.response, ast.literal_eval(expect)):
                    Logger().info(
                            "【第{}条用例用例名称为：{}---执行成功，结果返回值为：{}，期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id),"Pass",GetCurrentTime().get_curr_time())
                else:
                    Logger().error(
                            "【第{}条用例名称为：{}--执行失败！！,结果返回值为:{},期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id),str(self.response),GetCurrentTime().get_curr_time())
                    self.check.result()
            Logger().end_case(int(case_id),case_name)

if __name__ == '__main__':
    unittest.main()