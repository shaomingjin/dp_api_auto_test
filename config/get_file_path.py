#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 8:52
# @Author : ShaoMingJin

import os

class GetFilePath():

    @classmethod
    def get_path(self):
        '''
        获取项目路径下某个文件的绝对路径的方法，并返回
        :return:
        '''
        path=os.path.split(os.path.realpath(__file__))[0]
        return path

if __name__ == '__main__':
    print("项目的绝对路径为：",GetFilePath.get_path())
