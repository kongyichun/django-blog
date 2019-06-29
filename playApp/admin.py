from django.contrib import admin
from playApp.models import UserPost
from playApp.models import Users

# Register your models here.

admin.site.register(Users)
admin.site.register(UserPost)