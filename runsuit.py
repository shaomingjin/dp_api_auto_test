#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 0011 下午 14:40
# @Author : ShaoMingJin

import time, os, unittest
import pandas as pd
from util.HTMLTestRunner import HTMLTestRunner
from util.send_Email import SendEmail
import os
from util.read_config import ReadConfig
from util.logger import Logger

is_send_mail=ReadConfig.get_email("on_off") #获取发送邮件开关

class TestRunner(object):
    ''' Run test '''

    def __init__(self, cases="./case", title=u'API自动化测试报告', description="用例执行情况"):
        self.cases = cases
        self.title = title
        self.des = description
        self.send_email_to_conact=SendEmail()
        self.report_path=r'./report/'

    def run(self):

        #循环测试报告目录，并清空目录，保证测试报告目录下只保留最新的测试报告
        for filename in os.listdir(self.report_path):
            f = str(self.report_path + filename)  # 使用绝对路径
            if os.path.isdir(f):  # 判断是文件夹还是文件
                if not os.listdir(f):  # 判断文件夹是否为空
                    pass
                else:
                    break
            else:
                #循环删除测试所有的测试报告
                os.remove(f)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./report/" + now + "_result.html", 'wb')
        tests = unittest.defaultTestLoader.discover("./case", pattern='test*.py', top_level_dir=None) #执行case目录下所有的测试用例
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des,tester="Shaomj")  #生成测试报告
        runner.run(tests) #运行测试
        fp.close()
        #根据开关判断是否需要发邮件
        if is_send_mail=='on' or is_send_mail=='ON':
            self.send_email() #调用发送邮件方法
        else:
            Logger().info("所有测试用例已运行完毕，测试结束！")

    def send_email(self):
        '''
        统计成功和失败个数，并调用发送邮件
        :return:
        '''
        count_pass, count_fail = self.count_pass_fail_num()
        self.send_email_to_conact.send_main(count_pass,count_fail,self.get_file_name())

    def count_pass_fail_num(self):
        '''
        统计成功测试用例和失败测试用例个数，并返回
        :return:
        '''
        path = r'.\data\test.xls'
        data = pd.DataFrame(pd.read_excel(path))  # 读取数据,设置None可以生成一个字典，字典中的key值即为sheet名字，此时不用使用DataFram，会报错
        pass_count = 0
        fail_count =0
        for value in data['实际结果'].values:
            if value == "Pass" or value == "pass":
                pass_count+=1
            else:
                fail_count +=1
        return pass_count,fail_count

    def get_file_name(self):
        '''
        在report目录下获取最新生成的测试报告文件
        :return:
        '''
        file_name=[]
        for maindir,subdir,file_name_list in os.walk(self.report_path):
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                file_name.append(apath)
        return file_name[-1]


if __name__ == '__main__':
    run_testcase = TestRunner()
    run_testcase.run()
    #print((run_testcase.get_file_name()))



