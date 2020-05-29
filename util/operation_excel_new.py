#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 0009 下午 18:42
# @Author : ShaoMingJin

import xlrd,time
import xlwt
from util.get_projectpath import GetProjectPath
from xlutils.copy import copy

class OperationExcel(object):

    def __init__(self,file_name,sheet_id):
        # 获取myProject，也就是项目的根路径
        self.file_path =GetProjectPath().get_projectPath() +"data\\"+file_name
        self.sheet_id=sheet_id
        self.data=self.get_data()
        self.tmp_time = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

    def get_data(self):
        '''
        获取sheets的内容
        :return:
        '''
        # 打开Excel
        data=xlrd.open_workbook(self.file_path)
        # 获取某个sheet的内容
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lins(self):
        '''
        # 获取sheet的行数,
        # 例如：4行
        :return:
        '''
        tables=self.data
        return tables.nrows


    def get_cell_value(self,row,col):
        '''
        #获取某一个单元格的内容
        :param row:
        :param col:
        :return:
        '''
        tables=self.data
        cell=tables.cell_value(row,col)
        return cell


    def write_value(self,row,col,value):
        '''
        #写入数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style.alignment = al
        read_data=xlrd.open_workbook(self.file_path,formatting_info=True)  #formatting_info=True，按原来样式打开
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row, col, value,style)
        write_data.save(self.file_path)

    def get_rows_data(self,case_id):
        '''
        # 根据对应case_id找到对应行的内容
        :param case_id:
        :return:
        '''
        row_num = self.get_row_num(case_id)
        return self.get_row_values(row_num)


    def get_row_num(self, case_id):
        '''
         # 根据对应的case_id找到对应的行号
        :param case_id:
        :return:
        '''
        num = 0
        cols_data = self.get_cols_values()
        for data in cols_data:
            if case_id in data:
                return num
            num += 1
        return num

    def get_row_values(self, row):
        '''
        # 根据行号，找到该行的数据
        :param row:
        :return:
        '''
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    def get_cols_values(self, col_id=None):
        '''
        根据列号，找到该列的数据
        :param col_id:
        :return:
        '''
        if col_id != None:
            col = self.data.col_values(col_id)
        else:
            col = self.data.col_values(0)
        return col

if __name__ == '__main__':
    opexcel=OperationExcel("test.xlsx",0)
    print(opexcel.get_data())


