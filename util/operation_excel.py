#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 0009 下午 17:42
# @Author : ShaoMingJin

import xlrd,time
import xlwt
from util.logger import Logger
from util.get_projectpath import GetProjectPath
from xlutils.copy import copy

class OperationExcel(object):

    def __init__(self,file_name,sheet_id):
        if sheet_id!=None:
            # 获取myProject，也就是项目的根路径
            self.file_path = GetProjectPath().get_projectPath() + "data\\"+file_name
            self.sheet_id=sheet_id
        else:
            self.sheet_id=0
        self.data = self.get_datas()

    def get_datas(self):
        '''
        新建读取测试数据方法
        :return:
        '''
        # 定义空列表
        datas = []
        try:
            #打开指定文件
            xl = xlrd.open_workbook(self.file_path)
            #根据sheetName获取指定的sheet
            sheet = xl.sheet_by_index(self.sheet_id)
            items = sheet.row_values(0)
            #遍历excel的行数
            for nrow in range(1,sheet.nrows):
                #定义字典
                data = dict()
                values = sheet.row_values(nrow)
                for ncol in range(0,len(items)):
                    data[items[ncol]]=values[ncol]
                datas.append(data)
        except Exception as e:
            Logger().error("读取文件出错：{}".format(e))
        return datas

    def get_data_by_api_name(self,api_name):
        '''
        根据接口名称读取相关测试数据方法
        :param api_name:
        :return:
        '''
        # 新建空列表，添加读取Excel数据s
        arrs = []
        # 历Excel表格数据，并取值
        for data in self.data:
            if data.get("接口名称")==api_name:
                arrs.append((data.get("Id"),
                             data.get("接口名称"),
                             data.get("用例名称"),
                             data.get("url"),
                             data.get("是否运行"),
                             data.get("请求方式"),
                             data.get("请求头header"),
                             data.get("请求数据"),
                             data.get("期望结果"),
                             data.get("实际结果"),
                             data.get("优先级"),
                             data.get("运行时间")))
        return arrs

    def get_all_data(self):
        '''
        读取Excel表格中所有的数据
        :return:
        '''
        # 新建空列表，添加读取Excel数据s
        arrs = []
        # 遍历Excel表格数据，并取值
        for data in self.data:
            arrs.append((data.get("Id"),
                        data.get("接口名称"),
                        data.get("用例名称"),
                        data.get("url"),
                        data.get("是否执行"),
                        data.get("请求方式"),
                        data.get("请求头header"),
                        data.get("请求数据"),
                        data.get("预期结果"),
                        data.get("实际结果"),
                        data.get("优先级"),
                        data.get("运行时间")))
        return arrs

    def write_value(self,row, col, value):
        '''
             写入excel数据
             row,col,value
             '''
        tmp_time=time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))  #时间戳
        #Excel文件格式,红色
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
        al = xlwt.Alignment()
        al.horz = 0x02      # 设置水平居中
        al.vert = 0x01      # 设置垂直居中
        style0.alignment = al
        # 打开指定文件
        
        read_data = xlrd.open_workbook(self.file_path,formatting_info=True)  #formatting_info=True  保留原有的格式
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value,style0)
        write_data.save(self.file_path)


if __name__ == '__main__':
    filename="test.xls"
    opera=OperationExcel(filename,0)
    # print(opera.get_data_by_api_name("myUserallinfo"))






