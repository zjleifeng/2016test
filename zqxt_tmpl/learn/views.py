#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    #string=u'这里是显示的字符串变量'
    #TutorialList=['css','python','django','html']
    #info_dict={"site":u'python学习','content':u'各种python资料'}
    List=map(str,range(100))
    return render(request, 'home.html', {'List':List})


def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))

