#coding:utf-8
import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ipath='E:\py笔记\面试题'
uipath = unicode(ipath , "utf-8")

file_name='面试题.pdf'


#定义发送接受邮箱
mail_host='smtp.163.com'
mail_user='z_j_boy'
mail_pass='hello1105'
sender='z_j_boy@163.com'
receiver='7836567@qq.com'


#构造邮件附件

message=MIMEMultipart()
message['From']='z_j_boy@163.com'
message['To']='7836567@qq.com'

#标题
subject='会员资料信息'
message['Subject']=os.path.basename(file_name)

#正文

message.attach(MIMEText('会员资料信息如下附件：','plain','utf-8'))


#添加附件1

att1=MIMEText(open(os.path.join(uipath,file_name),'rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
#显示附件名字
att1.add_header('Content-Disposition','attachment',filename=('utf-8', '',file_name))
message.attach(att1)


#发送邮件
try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print '发送成功！'
except smtplib.SMTPException:
    print '发送失败！'