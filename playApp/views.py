from django.shortcuts import render
from playApp.models import User
from playApp import models
from django.http import HttpResponseRedirect
from playApp.forms import NameForm



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
    for u in User.objects.all():
        print(u.age)
    return render(request, '../templates/index.html')