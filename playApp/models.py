from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()

    class Meta:
        db_table = "User"


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class UserPost(models.Model):
    user_id = models.CharField(max_length=32)
    article_name = models.CharField(max_length=200)
    content = models.TextField