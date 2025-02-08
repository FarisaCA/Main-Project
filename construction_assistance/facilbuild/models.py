from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class login_tbl(AbstractUser):
    usertype=models.CharField(max_length=100)
class Contractor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    cmp_name=models.CharField(max_length=100)
    srv_cat=models.CharField(max_length=100)
    expc=models.CharField(max_length=100)
    certi=models.ImageField(max_length=None)
    wrk_hrs=models.CharField(max_length=100)
    user=models.ForeignKey(login_tbl, on_delete=models.CASCADE,null=True)
class Worker(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    skills=models.CharField(max_length=100)
    expc=models.CharField(max_length=100)
    user=models.ForeignKey(login_tbl, on_delete=models.CASCADE,null=True)
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)