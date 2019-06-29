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
    if request.session.get('is_login', None):
        return HttpResponseRedirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Users.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
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
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return HttpResponseRedirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return HttpResponseRedirect("/index/")


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return HttpResponseRedirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, '../templates/register.html', locals())
            else:
                same_name_user = models.Users.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, '../templates/register.html', locals())
                same_email_user = models.Users.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, '../templates/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Users.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return HttpResponseRedirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, '../templates/register.html', locals())