from django.shortcuts import render
from playApp.models import User

def index(request):
    return render(request, 'index.html')

def search(request):
    # from django.db import connection, connections
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute("SELECT * from User where id = 1")
    # row = cursor.fetchone()
    # print("search result:",end='')
    # print(row)
    for u in User.objects.all():
        print(u.age)
    return render(request, 'index.html')