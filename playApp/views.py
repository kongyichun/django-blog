from django.shortcuts import render
from playApp.models import User
from playApp import models


def index(request):
    user_list = models.UserInfo.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库
        if username and password:
            result = models.UserInfo.objects.filter(user=username)
            if not len(result):
                models.UserInfo.objects.create(user=username, pwd=password)
    return render(request, '../templates/index.html',{'data': user_list})


def post(request):
    return render(request, '../templates/post.html')


def comment(request):
    return render(request, '../templates/comment.html')


def about(request):
    return render(request, '../templates/about.html')


def search(request):
    for u in User.objects.all():
        print(u.age)
    return render(request, '../templates/index.html')