from django.db import models

# Create your models here.
class ContactForm(models.Model):
    topic=models.CharField()
    message=models.CharField()
