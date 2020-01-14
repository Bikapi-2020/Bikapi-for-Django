from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
from .models import B_User, B_Topic
from django.db import models
from .myforms import UserForm, RegisterForm
import hashlib

# Create your views here.


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def index(request):
    '''网站首页'''
    template = get_template('bikapi/index.html')
    buser = B_User.objects.all()
    btopic = B_Topic.objects.get(b_topic_id=1)
    html = template.render(locals())

    return HttpResponse(html)

def login(request):
    '''登录'''
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)
        message = "请检查填写内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = B_User.objects.get(b_user_name=username)
                if user.b_user_password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.b_user_id
                    request.session['user_name'] = user.b_user_name
                    request.session['user_id'] = user.b_user_id
                    return redirect('/index/')
                else:
                    message = '密码不正确！'
            except:
                message = '用户名不存在！'
                # return render(request, 'bikapi/login.html')
        return render(request, 'bikapi/login.html', locals())

    login_form = UserForm()
    return render(request, 'bikapi/login.html', locals())

def register(request):
    '''注册'''
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            # email = register_form.cleaned_data['email']
            role = register_form.cleaned_data['role']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'bikapi/register.html', locals())
            else:
                same_name_user = B_User.objects.filter(b_user_name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'bikapi/register.html', locals())
                # same_email_user = models.User.objects.filter(email=email)
                # if same_email_user:  # 邮箱地址唯一
                #     message = '该邮箱地址已被注册，请使用别的邮箱！'
                #     return render(request, 'bikapi/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = B_User.objects.create()
                new_user.b_user_name = username
                new_user.b_user_password = hash_code(password1)
                # new_user.email = email
                new_user.b_user_role = role
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'bikapi/register.html', locals())

def logout(request):
    '''注销'''
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def forum(request):
    '''论坛首页'''
    template = get_template('bikapi/forum.html')
    topic = B_Topic.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

def zone(request):
    '''论坛分区页'''
    return HttpResponse('论坛分区页')

def section(request):
    '''论坛版块页'''
    return HttpResponse('论坛版块页')

def topic(request,id):
    '''帖子详情页'''
    template = get_template('bikapi/topicinfo.html')
    btopic = B_Topic.objects.get(b_topic_id=id)
    # btopic2 = B_Topic.objects.all()
    html = template.render(locals())

    return HttpResponse(html)
    # return HttpResponse('帖子详情页')

def topic_comicon(reqyest):
    '''漫展列表页'''
    template = get_template('bikapi/topic_comicon.html')
    btopic = B_Topic.objects.get(b_topic_id=1)
    btopic2 = B_Topic.objects.all()
    html = template.render(locals())

    return HttpResponse(html)

def topic_baike(request):
    '''皮站百科'''
    template = get_template('bikapi/topic_baike.html')
    btopic = B_Topic.objects.get(b_topic_id=1)
    btopic2 = B_Topic.objects.all()
    html = template.render(locals())

    return HttpResponse(html)

def tag(request):
    '''标签页'''
    return HttpResponse('标签页')

def top(request):
    '''排行榜'''
    return HttpResponse('排行榜')

def userinfo(request,userid):
    '''用户首页'''
    template = get_template('bikapi/userinfo.html')
    user = B_User.objects.get(b_user_id=userid)
    html = template.render(locals())

    return HttpResponse(html)

def release(request):
    '''发帖'''
    return HttpResponse('发帖')
