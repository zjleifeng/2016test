#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'z_j_boy@163.com'
receiver = '7836567@qq.com'
subject = '放假通知'
smtpserver = 'smtp.163.com'
username = 'z_j_boy'
password = 'hello1105'

msg = MIMEText('大家关好窗户','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'Tim<z_j_boy@163.com>'
msg['To'] = "7836567@qq.com"


smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()