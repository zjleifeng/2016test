#coding:utf-8

from email.header import Header
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import Encoders

mail_host='smtp.163.com'
mail_user='z_j_boy'
mail_pass='hello1105'

sender='z_j_boy@163.com'
receiver='7836567@qq.com'

message=MIMEMultipart()

message['From']='z_j_boy@163.com'
message['To']='7836567@qq.com'

subject='带附件测试邮件发送'
message['Subject']=Header(subject,'utf-8')


#正文
message.attach(MIMEText('一下是附件内容哦','plain','utf-8'))

#构造附件1
att1=MIMEText(open('mianshi.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
#附件显示的名字任意写
att1["Content-Disposition"] = 'attachment; filename="mianshi.txt"'
message.attach(att1)

#附件2
att2=MIMEApplication(open('mianshi.pdf','rb').read())
att2.add_header('Content-Disposition','attachment',filename=('gbk', '', 'mianshi.pdf'))
message.attach(att2)

#附件3
att3=MIMEApplication(open(u'mianshi副本.pdf','rb').read())

att3["Content-Type"] = 'application/octet-stream'
att3.add_header('Content-Disposition','attachment',filename=('gbk', '','mianshi副本.pdf'))
#att3.add_header('Content-Disposition', u'attachment; filename="mianshi副本.pdf"')
Encoders.encode_base64(att3)
message.attach(att3)

#附件4
att4=MIMEApplication(open(u'mianshi副本.pdf','rb').read())

att4["Content-Type"] = 'application/octet-stream'
att4.add_header('Content-Disposition','attachment',filename=('utf-8', '','mianshi副本.pdf'))
#att3.add_header('Content-Disposition', u'attachment; filename="mianshi副本.pdf"')
Encoders.encode_base64(att4)
message.attach(att4)


try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print '成功发送'
except smtplib.SMTPException:
    print '失败'