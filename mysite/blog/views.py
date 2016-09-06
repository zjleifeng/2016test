from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader,context
from django.http import HttpResponse
from blog.models import BlogPost


"""
def archive(request):
    posts=BlogPost.objects.all()
    t=loader.get_template("archive.html")
    c=context({'posts':posts})
    return HttpResponse(t.render(c))
# Create your views here.
"""


def index(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})