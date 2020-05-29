#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 0010 下午 14:24
# @Author : ShaoMingJin

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from util.logger import Logger
from email.header import Header
import smtplib
from util.read_config import ReadConfig

email_host=ReadConfig.get_email('email_host')
send_user = ReadConfig.get_email('send_user') #"autotest_123@163.com" #发送者
password =ReadConfig.get_email('password') #"ZVDAJLUUHWYPADQW"  #授权码
receive_user=ReadConfig.get_email("rec_user")#接受邮件的人
sub =ReadConfig.get_email("sub")#"邮件主题"


#新建发邮件类
class SendEmail(object):

     def send_mail(self,user_list,sub,content,new_testReport_file):
         '''
         定义发送邮件方法
         :param user_list:
         :param sub:
         :param content:
         :param new_testReport_file:
         :return:
         '''
         user = "AutoTest"+"<"+send_user+">"
         msg = MIMEMultipart()
         msg["Subject"] = Header(s=sub, charset="utf-8")  # 标题
         msg["From"] = Header(s=user)  # 发送者
         msg["To"] = Header(s='; '.join(user_list))  # 接收者
         Logger().info("收件人为：{}".format(user_list))
         # 邮件正文
         msg.attach(payload=MIMEText(_text=content, _subtype="plain", _charset="utf-8"))
         # 附件1
         att1 = MIMEText(_text=open(new_testReport_file, "rb").read(), _subtype="base64", _charset="utf-8")
         att1["Content-Type"] = "application/octet-stream"
         att1["Content-Disposition"] = "attachment; filename=%s" %'TestReport.html'  # filename 可以任意写，写什么名字，邮件中显示什么名字。但是不要写中文
         msg.attach(payload=att1)

         server = smtplib.SMTP() #声明邮件服务器对象
         server.connect(email_host) #链接邮箱服务器
         server.login(send_user,password) #利用授权码登录邮箱
         server.sendmail(user,user_list,msg.as_string()) #发送邮件
         server.quit()
         Logger().info("发送邮件成功，收件人为：{}".format(user_list))

     def send_main(self,pass_num,fail_num,new_testReport_file):
         count_num = pass_num+fail_num
         pass_result = "%.2f" %float(pass_num/count_num*100)
         fail_result = "%.2f" %float(fail_num/count_num*100)
         user_list =[receive_user]
         #邮件正文
         content_text = "各位同仁们：\n" \
          "  本次自动化测试一共运行测试用例个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )+"\n"
         # 添加测试报告附件
         self.send_mail(user_list,sub,content_text,new_testReport_file)

if __name__ == '__main__':
     sen = SendEmail()
