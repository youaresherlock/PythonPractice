# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-09-10 15:50:57
# @Last Modified by:   Clarence
# @Last Modified time: 2018-09-10 18:04:37
"""
发送带附件的邮件
发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.qq.com" # 设置服务器
#自己的邮箱，通过QQ邮箱设置获取口令
mail_user = "2263194561@qq.com" #用户名
mail_pass = "edhrfxbglitheccb" # 口令

sender = '2263194561@qq.com'
receivers = ['1430371727@qq.com'] #接受者的邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("发送邮件者Clarence", 'utf-8')
message['To'] = Header("xxxxxxxxxxxxxxxxx@qq.com", 'utf-8')
subject = 'Python SMTP  邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是smtp协议发送邮件测试有效负载内容....', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件，可以看出是直接读取文本二进制流
attr1 = MIMEText(open('test1.txt', 'rb').read(), 'base64', 'utf-8') 
"""
上行代码作用
Content-Type: text/base64; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
"""
attr1["Content_Type"] = 'application/octet-stream' # 内容是二进制流，不知道文件类型
# 
attr1["Content-Disposition"] = 'attachment; filename="send1.txt"' #Content-Disposition是MIME协议的扩展，支持MIME用户代理如何显示附加的文件
message.attach(attr1)

#构造附件2，传送当前目录下的test2.txt文件
attr2 = MIMEText(open('test2.txt', 'rb').read(), 'base64', 'utf-8')
attr2["Content_Type"] = 'application/octet-stream' 
attr2['Content-Disposition'] = 'attachment; filename="send2.txt'
message.attach(attr2)

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25) # 25为SMTP端口号
	smtpObj.login(mail_user, mail_pass) #会返回(状态码, "字符串解释")元组信息
	smtpObj.sendmail(sender, receivers, message.as_string())
	print(message)
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")