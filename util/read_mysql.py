#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 23:00
# @Author : ShaoMingJin

import pymysql
from util.read_config import ReadConfig
from util.logger import Logger

'''
常用模块，读写mysql
'''
host=ReadConfig.get_database_info('sqlserver')#获取数据库服务器地址
user=ReadConfig.get_database_info('user_root') #获取数据库登录用户
password=ReadConfig.get_database_info('password_root') #获取用户密码
database=ReadConfig.get_database_info('database_root') #获取数据库
port=int(ReadConfig.get_database_info('port_database')) #获取数据库端口
charset=ReadConfig.get_database_info('charset_database') #获取字符编码

class ReadMySql():

    @classmethod
    def get_conn(self):
        '''
        获取mysql的链接
        :return: mysql connection
        '''
        try:
            conn = pymysql.connect(host=host, user=user, password=password,database=database, port=port, charset=charset)
            Logger().error("链接数据库成功！！")
            return conn
        except:
            Logger().error("链接数据库异常！！")

    @classmethod
    def query_data(self,sql):
        '''
        根据sql查询数据并且返回
        :param sql:
        :return: list[dict]
        '''
        conn =ReadMySql.get_conn()
        try:
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            Logger().error("查询数据库成功！！")
            return  cursor.fetchall()
        except:
            Logger().error("查询数据库异常！！")
        finally:
            conn.close()

    @classmethod
    def insert_or_update_data(self,sql):
        '''
        执行新增insert或者update的sql
        :param sql:
        :return: 不返回内容
        '''

        conn=self.get_conn()
        try:
            cursor=conn.cursor()
            cursor.execute(sql)
            conn.commit()
            Logger().error("更新数据库成功！！")
        except:
            Logger().error("更新数据库异常！！")
        finally:
            conn.close()


if __name__ == '__main__':
    sql="SELECT * FROM student"
    list =ReadMySql.query_data(sql)
    print(list)





