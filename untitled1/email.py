#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
#from email.mime.text import MIMEText

mail_host='smtp.163.com'
mail_user='z_j_boy'
mail_pass='hello1105'

sender='z_j_boy@163.com'
receiver=['7836567@qq.com']
message=MIMEText('python测试邮件','plain','utf-8')
message['From']='Tim<z_j_boy@163.com>'
message['To']="7836567@qq.com"

subject='python smtp 测试邮件'
message['Subject']=Header(subject,'utf-8')


try:
    smtpobj=smtplib.SMTP()
    smtpobj.connect(mail_host)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receiver,message.as_string())
    print '成功'
except smtplib.SMTPException:
    print '错误'