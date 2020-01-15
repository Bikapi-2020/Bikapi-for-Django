from django import forms
from captcha.fields import CaptchaField
from datetime import datetime


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    role = (
        ('1', '摄影师'),
        ('2', 'Coser'),
        ('3', '二次元er'),
    )
    username = forms.CharField(label="用户名", max_length=128, error_messages={
        'required': '用户名不能为空'
    },widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="密码", max_length=256,error_messages={
        'required': '密码不能为空'
    }, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    role = forms.ChoiceField(label='角色', choices=role)

    avatar = forms.FileField(label='头像', required=False)

    captcha = CaptchaField(label='验证码')

class SetPassword(forms.Form):

    passwordset = forms.CharField(label="原密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    passwordset1 = forms.CharField(label="修改密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    passwordset2 = forms.CharField(label="确认修改密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
