from django.db import models
from django import forms


class Users(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['c_time']
        verbose_name = 'BlogUser'
        verbose_name_plural = 'BlogUsers'


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class UserPost(models.Model):
    article_name = models.CharField(max_length=200)
    content = models.TextField()
