# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-09-10 11:25:25
# @Last Modified by:   Clarence
# @Last Modified time: 2018-09-10 13:35:17
"""
如果本机没有sendmail访问，可以使用其他服务商的SMTP访问(QQ、网易、Google等)
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.XXX.com" # 设置服务器
mail_user = "XXXXX" #用户名
mail_pass = "XXXXXXXXX" # 口令

sender = 'from@runoob.com'
receivers = ['2263194561@qq.com'] #接受邮件

message  = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP  邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect()