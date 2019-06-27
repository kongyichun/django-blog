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


def search(request):
    # from django.db import connection, connections
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute("SELECT * from User where id = 1")
    # row = cursor.fetchone()
    # print("search result:",end='')
    # print(row)
    for u in User.objects.all():
        print(u.age)
    return render(request, '../templates/index.html')