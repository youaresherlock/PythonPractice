# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-29 22:52:18
# @Last Modified by:   Clarence
# @Last Modified time: 2018-09-10 11:25:00

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

sender = 'smtp.mandrillapp.com'
receivers = ['2263194561@qq.com'] #接受邮件，可以设置为你的QQ邮箱或者其他邮箱

# 三个参数: 第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
"""
MIME类型(Multipurpose Internet Mail Extensions)是描述消息内容类型的因特网标准
MIME消息能包含文本、图像、音频、视频以及其他应用程序专用的数据
不同的应用程序支持不同的MIME类型
"""
message = MIMEText('Python邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", "utf-8") #发送者
message['To'] = Header('测试', 'utf-8') # 接受者

subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
	print(type(message), message)
	smtpObj = smtplib.SMTP('localhost') 
	smtpObj.sendmail(sender, receivers, message.as_string())
	print('邮件发送成功')
except smtplib.SMTPException:
	print("Error: 无法发送邮件") 

"""
<class 'email.mime.text.MIMEText'> Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
From: =?utf-8?b?6I+c6bif5pWZ56iL?=
To: =?utf-8?b?5rWL6K+V?=
Subject: =?utf-8?b?UHl0aG9uIFNNVFDpgq7ku7bmtYvor5U=?=

UHl0aG9u6YKu5Lu25Y+R6YCB5rWL6K+VLi4u
可以看到打印出来的message这个MIME文本类，里面包含的内容是编码类型，数据类型，MIME版本，以及传输的编码格式base64,
下面是邮件的首发地址，可以看到这是用base64编码之后的地址

//这里出现由于目标计算机积极拒绝，无法连接错误的原因是，邮件服务器需要认证登陆,大家可以在linux或者win配置sendmail服务端，然后尝试
smtp = smtplib.SMTP_SSL(smtpserver, 465)
smtp.helo()
smtp.ehlo()
smtp.login(user, password)来认证 
"""