#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/8 0008 下午 19:50 
# @Author : ShaoMingJin
'''
目标：实现登录接口业务层，并且测试数据参数化（通过ddt)
注意：pip install parameterized
'''
#导入包
import unittest,json,ast,ddt
from util.verify_testresult import CheckPoint
from api.api_login_excel import ApiLogin
from util.logger import Logger
from util.operation_excel import OperationExcel
from util.read_config import ReadConfig
from data.get_data_fromexcel import GetDataFromExcel
from util.get_current_time import GetCurrentTime

#新建测试类
@ddt.ddt
class TestLogin(unittest.TestCase):

    #构造函数
    def setUp(self):
        self.getdata=GetDataFromExcel("test.xls", 0)
        self.check=CheckPoint()

    @ddt.data(*OperationExcel("test.xls", 0).get_data_by_api_name("login"))
    def test_login(self,test_data):

        #获取测试用例的所有列的值
        case_id,api_name,case_name,url,is_run,request_method,header,request_data,expect,result,prority,run_time=tuple(test_data)

        if is_run == "yes":   # 判断测试用例是否需要运行
            Logger().start_case(int(case_id),case_name)
            url=ReadConfig.get_host("url")+url #拼接接口url
            # 调用接口请求方法
            self.response = ApiLogin().api_post_login(url, request_method, header, request_data) #获取接口响应数据
            if int(prority) == 1:  #根据优先级按顺序执行
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
                if self.check.is_equal(check_point,ast.literal_eval(expect)):
                    Logger().info(
                        "【第{}条测试用例;测试用例名称为：{}--执行成功，结果返回值为：{}，期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    #把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id),"Pass",GetCurrentTime().get_curr_time())
                else:
                    Logger().error(
                        "【第{}条测试用例;测试用例名称为：{}--执行失败！！，结果返回值为：{}，期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把错误的测试用例的响应数据回写到相应的实际结果中
                    self.getdata.update_excel(int(case_id), str(self.response), GetCurrentTime().get_curr_time())
                    self.check.result()
            else:
                if self.check.is_equal(self.response,ast.literal_eval(expect)):
                    Logger().info(
                        "【第{}条测试用例;测试用例名称为：{}---执行成功，结果返回值为：{}，期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id), "Pass", GetCurrentTime().get_curr_time())
                else:
                    Logger().error(
                        "【第{}条测试用例;测试用例名称为：{}--执行失败！！,结果返回值为:{},期望结果为：{}】".format(int(case_id), case_name, self.response, expect))
                    # 把测试结果回写到Excel表中
                    self.getdata.update_excel(int(case_id), str(self.response), GetCurrentTime().get_curr_time())
                    self.check.result()
            Logger().end_case(int(case_id),case_name)

if __name__ == '__main__':
    unittest.main()
