#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 0009 上午 10:26
# @Author : ShaoMingJin

import time
import hashlib

class GetMD5(object):

    #获取时间
    def get_time(self):
        return str(int(time.time()))

    def get_sign(self,sign):
        '''
        MD5对签名加密
        :param sign:
        :return:
        '''
        self.hash_md5=hashlib.md5()
        self.hash_md5.update(sign.encode("utf8"))
        self.hash_sha1 = hashlib.sha1()
        self.hash_sha1.update(self.hash_md5.hexdigest().encode("utf8"))
        return self.hash_sha1.hexdigest()
