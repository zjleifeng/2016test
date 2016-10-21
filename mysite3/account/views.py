#coding=utf-8

from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User
from sendmail1 import send

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import chardet
# Create your views here.

class UserFrom(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'username','placeholder':'用户名'}))
    #username=forms.CharField(label="", max_length=100)
    password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class': 'password','placeholder':'密  码'}))
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'email','placeholder':'电子邮件'}))
    qq=forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'qq','placeholder':'Q Q'}))

class UserLoginFrom(forms.Form):
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'username','placeholder':'用户名'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'password','placeholder':'密码'}))

class ConnectForm(forms.Form):
    name=forms.CharField(error_messages={'required': '请输入姓名'},label='',widget=forms.TextInput(attrs={'class':'username','placeholder':'姓名'}))
    mail=forms.EmailField(error_messages={'required': '请输入邮箱'},label='',widget=forms.TextInput(attrs={'class':'email','placeholder':'邮箱'}))
    qcq=forms.CharField(error_messages={'required': '请输入QQ'},label="",widget=forms.TextInput(attrs={'class': 'qq','placeholder':'Q Q'}))
    phone=forms.IntegerField(error_messages={'required': '请输入手机号码'},label="",widget=forms.TextInput(attrs={'class': 'phone','placeholder':'手机'}))
    ytext=forms.CharField(error_messages={'required': '请输入您的需求'},label='',widget=forms.Textarea(attrs={'class':'Message','placeholder':'留言'}))



def register(request):
        if request.method == "POST":
            uf=UserFrom(request.POST)
            if uf.is_valid():
                username=uf.cleaned_data['username']
                password=uf.cleaned_data['password']
                email=uf.cleaned_data['email']
                qq=uf.cleaned_data['qq']
                userResult = User.objects.filter(username=username,password=password)
                #error=[]
                filterResult = User.objects.filter(username = username)
                if len(filterResult)>0:
                    return render_to_response('hasregister.html',{'username':username})

                else:
                    user=User()
                    user.username=username
                    user.password=password
                    user.email=email
                    user.qq=qq
                    user.save()
                    return render_to_response('success.html',{'username':username})
        else:
            uf=UserFrom()
        return render_to_response('register.html',{'uf':uf})
"""
def login(request):
    if request.method=='POST':
        uf=UserLoginFrom(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user=User.objects.filter(username__exact=username,password__exact=password)
            if user:
                #render_to_response('loginsuc.html',{"username":username})
               # response.set_cookie('username',username,3600)
                response = HttpResponseRedirect('/account/loginsuc/')
                response.set_cookie('username',username,3600)
                return response
            else:
                response=HttpResponseRedirect('/account/register/')
    else:
        uf=UserLoginFrom()
        return render_to_response('register.html',{'uf':uf})

"""
def login(req):
    if req.method == 'POST':
        uf = UserLoginFrom(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                return render_to_response('index.html')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                #return HttpResponseRedirect('/account/login/')
                return render_to_response('login.html')
    else:
        uf = UserLoginFrom()
    return render_to_response('login.html',{'uf':uf})

def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def about(request):
    return render_to_response('about.html')

def features(request):
    return render_to_response('features.html')

def portfolio(request):
    return render_to_response('portfolio.html')

def contact(request):
    if request.method == "POST":
            cf=ConnectForm(request.POST)
            if cf.is_valid():
                name = cf.cleaned_data['name']
                bname=name.encode('utf-8')
                phone=cf.cleaned_data['phone']
                #yphone=phone.encode('utf-8')
                ytext = cf.cleaned_data['ytext']
                bmsg=ytext.encode('utf-8')
                mail = cf.cleaned_data['mail']
                bmail=mail.encode('utf-8')
                qcq = cf.cleaned_data['qcq']
                qq=qcq.encode('utf-8')


                reginfo="""
                客户注册信息

                姓名:%s
                手机:%s
                邮箱:%s
                QQ:%s
                留言:%s
                """%(bname,phone,bmail,qq,bmsg)

                huifu='资料已经收藏，我们会尽快与您联系！'



                sender = 'z_j_boy@163.com'
                receiver = '7836567@qq.com'
                subject = '新用户注册通知(重要！)'
                smtpserver = 'smtp.163.com'
                username = 'z_j_boy'
                password = 'hello1105'

                msg = MIMEText(reginfo,'plain')
                msg['Subject'] = Header(subject, 'utf-8')
                msg['From'] = '新客户注册通知<z_j_boy@163.com>'
                msg['To'] = "7836567@qq.com"


                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)
                smtp.login(username, password)
                smtp.sendmail(sender, receiver, msg.as_string())
                smtp.quit()
                #return render_to_response('success.html.html',{'username': chardet.detect(name)})
                return render_to_response('success.html',{'username':huifu})
            else:pass


    else:
        cf=ConnectForm()
    return render_to_response('contact.html',{'cf':cf})

