#coding:utf-8



import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host='smtp.163.com'
mail_user='z_j_boy'
mail_pass='hello1105'
sender = 'z_j_boy@163.com'
receivers = ['7836567@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From']='Tim<z_j_boy@163.com>'
message['To']="7836567@qq.com"

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"