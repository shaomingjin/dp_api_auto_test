#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/4/16 14:34 
# @Author : ShaoMingJin

import os

class GetProjectPath(object):

    def get_projectPath(self):
        '''
        定义方法,获取项目路径并返回
        :return:
        '''
        cur_path = os.path.abspath(os.path.dirname(__file__))
        root_path = cur_path[:cur_path.find("api_auto_test\\") + len("api_auto_test\\")]
        return root_path