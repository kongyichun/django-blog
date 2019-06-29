from django.shortcuts import render
from playApp import models
from playApp.models import UserPost
from playApp.models import UserInfo
# from playApp.models import Users
from django.http import HttpResponseRedirect
from playApp.forms import *


def index(request):
    post_list = models.UserPost.objects.all()
    return render(request, '../templates/index.html',{'data': post_list})


def post(request):
    # 如果form通过POST方法发送数据
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # 处理form.cleaned_data中的数据
            # ...
            # 重定向到一个新的URL
            models.UserPost.objects.create(article_name=request.POST.get('title'), content=request.POST.get('content'))
            return HttpResponseRedirect('/index/')

    # 如果是通过GET方法请求数据，返回一个空的表单
    else:
        form = NameForm()
    return render(request, '../templates/post.html', {'form': form})


def comment(request):
    return render(request, '../templates/comment.html')


def about(request):
    return render(request, '../templates/about.html')


def search(request):
    for u in Users.objects.all():
        print(u.age)
    return render(request, '../templates/index.html')


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Users.objects.get(name=username)
                if user.password == password:
                    return HttpResponseRedirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, '../templates/login.html', locals())

    login_form = UserForm()
    return render(request, '../templates/login.html',locals())


def register(request):
    pass
    return render(request, '../templates/register.html')


def logout(request):
    pass
    return HttpResponseRedirect('/index/')