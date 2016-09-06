#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders


def send(name,mail,qcq,ytext):

        sender = 'z_j_boy@163.com'
        #receiver = '7836567@qq.com'
        subject = '客户注册通知'
        smtpserver = 'smtp.163.com'
        username = 'z_j_boy'
        password = 'hello1105'
        receiver = '7836567@qq.com'
        message=MIMEText('客户姓名：','plain','utf-8')
        message['From']='Tim<z_j_boy@163.com>'
        message['To']=receiver
        message['Subject']=Header(subject,'utf-8')



        smtpObj=smtplib.SMTP()
        smtpObj.connect(smtpserver)
        smtpObj.login(username,password)
        smtpObj.sendmail(sender,receiver,message.as_string())
        smtpObj.quit()
