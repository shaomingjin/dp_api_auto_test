#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/16 1:50 
# @Author : ShaoMingJin

from util.operation_excel_new import OperationExcel
from data import data_excel
from  util.operation_json import OperationJson

class GetDataFromExcel:
    def __init__(self,file_name,sheet_id):
        self.oper_excel = OperationExcel(file_name,sheet_id)

    #去获取excel行数，就是case个数
    def get_case_lines(self):
        return self.oper_excel.get_lins()

    #获取case_id
    def get_case_id(self,ros):
        col=int(data_excel.get_id())
        case_id=self.oper_excel.get_cell_value(ros,col)
        return case_id

    #获取api_name
    def get_api_name(self,row):
        col=int(data_excel.get_api_name())
        api_name=self.oper_excel.get_cell_value(row,col)
        return api_name

    #获取case_name
    def get_case_name(self,row):
        col=int(data_excel.get_case_name())
        case_name=self.oper_excel.get_cell_value(row,col)
        return case_name

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_excel.get_run())
        run_model = self.oper_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_excel.get_request_way())
        request_method = self.oper_excel.get_cell_value(row,col)
        return request_method

    #获取url
    def get_request_url(self,row):
        col = int(data_excel.get_url())
        url = self.oper_excel.get_cell_value(row,col)
        return url

    # 获取请求头header
    def get_request_header(self,row):
        col = int(data_excel.get_header())
        data = self.oper_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data

    # # 通过获取头关键字拿到data数据
    # def get_header_value(self, row):
    #     oper_json = OperationJson('../dataconfig/request_header.json')
    #     request_header = oper_json.get_data(self.get_request_header(row))
    #     return request_header

    #获取请求数据
    def get_request_data(self,row):
        col = int(data_excel.get_request_data())
        data = self.oper_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    # #通过获取请求关键字拿到data数据
    # def get_data_value(self,row):
    #     oper_json = OperationJson('../dataconfig/request_data.json')
    #     request_data = oper_json.get_data(self.get_request_data(row))
    #     return request_data

    #获取优先级
    def get_prority(self,row):
        col=int(data_excel.get_prority())
        case_prority=self.oper_excel.get_cell_value(row,col)
        return case_prority

    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_excel.get_expect())
        expect = self.oper_excel.get_cell_value(row,col)
        return expect

    #写入数据
    def write_result(self,row,value):
        col = int(data_excel.get_result())
        self.oper_excel.write_value(row,col,value)

    #写入运行时间
    def write_run_time(self,row,value):
        col=int(data_excel.get_run_time())
        self.oper_excel.write_value(row,col,value)

    #根据case_id写入测试结果和用例运行时间
    def update_excel(self,row,testresult,runtime):
        self.write_result(row,testresult)
        self.write_run_time(row,runtime)



if __name__ == '__main__':
    file_name="test.xls"
    getdata=GetDataFromExcel(file_name,0)
    getdata.write_result(1,"Pass")
