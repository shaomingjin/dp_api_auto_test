#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/28 9:08 
# @Author : ShaoMingJin

import time

class GetCurrentTime():

    def get_curr_time(self):
        '''
        获取系统当前时间，并返回
        :return:
        '''
        curr_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return curr_time

if __name__ == '__main__':
    print(GetCurrentTime().get_curr_time())