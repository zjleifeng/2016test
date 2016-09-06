import smtplib
from_mail='z_j_boy@163.com'
to_mail='7836567@qq.com'
server=smtplib.SMTP('smtp.163.com')
server.docmd('ehlo','z_j_boy@163.com')
server.login('z_j_boy','hello1105')
msg='''from:xxx@126.com
to:yyy@qq.com
subject:I am guol
I'm come 126
.
'''
server.sendmail(from_mail,to_mail,msg)
server.quit()