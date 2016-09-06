from django.db import models
from django.contrib import admin
# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    qq=models.CharField(max_length=50)


class Useradmin(admin.ModelAdmin):
    list_display = ('username','email','qq')

admin.site.register(User,Useradmin)

