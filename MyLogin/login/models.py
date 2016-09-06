from django.db import models
from django.contrib import admin
from django import forms
import login

class RegisterForm(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=150)
    password2=models.CharField(max_length=150)

    def pwd_validate(self,p1,p2):
        return p1==p2

    def __unicode__(self):
        return self.username



class LoginForm(forms.Form):
    username=models.CharField()
    password=models.CharField()

    def __unicode__(self):
        return self.username


class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()

    def __unicode__(self):
        return self.username

class Useradmin(admin.ModelAdmin):
    list_display = ('username','email')

admin.site.register(User,Useradmin)