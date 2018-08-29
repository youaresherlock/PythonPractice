# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-29 22:52:18
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-29 23:53:06

"""
Python3 SMTP发送邮件
python的smtplib提供一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装
Python创建SMTP对象语法如下:
import smtplib
smtpObj = smtplib.SMTP( [host [, port[, local_hostname]]])
参数:
	host: SMTP服务器主机。你可以指定主机的ip地址或者域名字符串(本地'localhost').
	port: 如果你提供了host参数，你需要指定SMTP服务使用的端口号，一般情况下SMTP端口号为25
	local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为localhost即可
Python SMTP对象使用sendmail方法发送邮件，语法如下:
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
参数:
	from_addr: 邮件发送者地址
	to_addrs:字符串列表，邮件发送地址
	msg:发送消息 字符串，邮件一般有标题，发信人，收信人，邮件内容，附件等构成，发送邮件的时候，
	要注意msg的格式。这个格式就是smtp协议中定义的格式。
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@clarence.com'
receivers = ['2263194561@qq.com'] #接受邮件，可以设置为你的QQ邮箱或者其他邮箱

# 三个参数: 第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
