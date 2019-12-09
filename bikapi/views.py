from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
from .models import B_user
from django.db import models

# Create your views here.

def index(request):
    '''首页'''
    template = get_template('bikapi/index.html')
    buser = B_user.objects.all()
    html = template.render(locals())

    return HttpResponse(html)

def login(request):
    '''登录'''
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username & password:
            username = username.strip()
            try:
                user = models.B_user.objects.get(name=username)
                if user.b_password == password:
                    return register('index/')
                else:
                    message = '密码不正确！'
            except:
                message = '用户名不存在！'
        return render(request, 'bikapi/index.html', {'提示：':message})
    return render(request, 'bikapi/login.html' )

def register(request):
    '''注册'''
    pass
    return render(request, 'bikapi/register.html')

def logout(request):
    '''注销'''
    pass
    return render(request, 'bikapi/index.html')
