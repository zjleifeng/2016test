import smtplib
from_mail='84307409@qq.com'
to_mail='7836567@qq.com'
server=smtplib.SMTP('smtp.qq.com')
server.docmd('ehlo','84307409@qq.com')
server.login('84307409','zhangjun00')
msg='''from:xxx@126.com
to:yyy@qq.com
subject:I am guol
I'm come 126
.
'''
server.sendmail(from_mail,to_mail,msg)
server.quit()