from django.db import models
from datetime import datetime

# Create your models here.


class B_user(models.Model):
    b_uid = models.AutoField(primary_key=True)
    b_username = models.CharField(max_length=32, blank=False, unique=True, verbose_name='用户名')
    b_password = models.CharField(max_length=16, blank=False, verbose_name='用户密码')
    b_regdate = models.DateTimeField(auto_now_add=datetime.now(), verbose_name='注册日期')


    class Meta:
        ordering = ["b_uid"]
        verbose_name = '用户ID'
    def __str__(self):
        return str(self.b_username)
