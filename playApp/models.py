from django.db import models

# Create your models here.


class User(models.Model):
    age = models.BigIntegerField()

    class Meta:
        db_table = "User"