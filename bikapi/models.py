from django.db import models
from datetime import datetime

# Create your models here.


class B_user(models.Model):
    '''用户表'''

    role = (
        (1,'摄影师'),
        (2, 'Coser'),
        (3, '二次元er'),
    )

    # 用户ID
    b_uid = models.AutoField(primary_key=True)
    # 用户名
    b_username = models.CharField(max_length=32, blank=False, unique=True, verbose_name='用户名')
    # 用户密码
    b_password = models.CharField(max_length=16, blank=False, verbose_name='用户密码')
    # 注册时间
    b_regdate = models.DateTimeField(auto_now_add=datetime.now(), verbose_name='注册日期')
    # 角色选择
    b_role = models.CharField(max_length=32,choices=role,default=3)
    # 邮箱地址
    # email = models.EmailField(unique=True)

    class Meta:
        # 根据用户ID排序
        ordering = ["b_uid"]
        verbose_name = '用户名'
    def __str__(self):
        return str(self.b_username)