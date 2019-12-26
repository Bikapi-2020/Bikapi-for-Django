from django.db import models
from datetime import datetime
from django.utils.timezone import now

class B_User(models.Model):
    # '''普通用户表'''

    role = (
        ('1', '摄影师'),
        ('2', 'Coser'),
        ('3', '二次元er'),
    )
    sex = (
        ('1', '未选择'),
        ('2', '男'),
        ('3', '女'),
    )

    # 用户ID
    b_user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    # 用户名
    b_user_name = models.CharField(max_length=32, blank=False, verbose_name='用户名')
    # 用户密码
    b_user_password = models.CharField(max_length=255, blank=False, verbose_name='用户密码')
    # 注册时间
    b_user_regdate = models.DateTimeField(auto_now_add=datetime.now(), verbose_name='注册日期')
    # 角色选择
    b_user_role = models.CharField(max_length=32, choices=role, default='3', verbose_name='角色')
    # 邮箱地址
    b_user_email = models.EmailField(default='', blank=True)
    # 用户手机号码
    b_user_phone = models.CharField(max_length=16, blank=True, default='', verbose_name='手机号码')
    # 用户性别
    b_user_sex = models.CharField(max_length=32, choices=sex, default='1', verbose_name='性别')
    # 用户生日
    # b_user_birthday = models.DateField(default=now, verbose_name='生日')
    # 用户头像
    b_user_avatar = models.FileField(upload_to='static/images/', blank=True, verbose_name='头像')

    class Meta:
        # 根据用户ID排序
        ordering = ["b_user_id"]
        verbose_name = '用户名'
        verbose_name_plural = '用户'
    def __str__(self):
        return str(self.b_user_name)

class B_Manager(models.Model):
    '''管理员表'''
    # 管理员ID
    b_manage_id = models.AutoField(primary_key=True, verbose_name='管理员ID')
    # 管理员名
    b_manage_name = models.CharField(max_length=32, blank=False, verbose_name='管理员')
    # 管理员密码
    b_manage_password = models.CharField(max_length=16, blank=False, verbose_name='管理员密码')

    class Meta:
        # 根据用户ID排序
        ordering = ["b_manage_id"]
        verbose_name = '管理员'
        verbose_name_plural = '管理员'
    def __str__(self):
        return str(self.b_manage_name)


class B_Zone(models.Model):
    '''分区表'''
    # 分区ID
    b_zone_id = models.AutoField(primary_key=True, verbose_name='分区ID')
    # 分区名称
    b_zone_name = models.CharField(max_length=32, verbose_name='分区')

    class Meta:
        # 根据用户ID排序
        ordering = ["b_zone_id"]
        verbose_name = '论坛分区'
        verbose_name_plural = '论坛分区'
    def __str__(self):
        return str(self.b_zone_name)

class B_Section(models.Model):
    '''板块表'''
    # 板块ID
    b_section_id = models.AutoField(primary_key=True, verbose_name='板块ID')
    # 板块关联分区ID
    b_section_zone = models.ForeignKey(to='B_Zone', on_delete=models.PROTECT, verbose_name='分区ID')
    # 板块名称
    b_section_name = models.CharField(max_length=64, verbose_name='板块')
    # 板主编号
    b_section_uid = models.ForeignKey(to='B_User', on_delete=models.DO_NOTHING, verbose_name='版主编号')
    # 板块说明
    b_section_explanation = models.CharField(max_length=255, verbose_name='板块说明')
    # 板块点击次数
    b_section_num = models.IntegerField(default=0, verbose_name='板块点击次数')
    # 板块主题数
    b_section_count = models.IntegerField(default=0, verbose_name='板块主题数')
    # 板块分类

    class Meta:
        # 根据用户ID排序
        ordering = ["b_section_id"]
        verbose_name = '论坛板块'
        verbose_name_plural = '论坛板块'
    def __str__(self):
        return str(self.b_section_name)

class B_Topic2Tag(models.Model):
    '''标签多对多帖子表'''
    b_t2t_topic = models.ForeignKey(to='B_Topic', on_delete=models.DO_NOTHING)
    b_t2t_tag = models.ForeignKey(to='B_Tag', on_delete=models.DO_NOTHING)

class B_Topic(models.Model):
    '''帖子表'''
    # 帖子编号
    b_topic_id = models.AutoField(primary_key=True, verbose_name='帖子ID')
    # 帖子板块编号
    b_topic_section = models.ForeignKey(to='B_Section', on_delete=models.DO_NOTHING, verbose_name='板块ID')
    # 帖子作者编号
    b_topic_tuser = models.ForeignKey(to='B_User', on_delete=models.DO_NOTHING, verbose_name='帖子作者ID')
    # 帖子表情
    # 帖子标题
    b_topic_title = models.CharField(max_length=64, blank=True, verbose_name='标题')
    # 帖子摘要
    b_topic_desc = models.CharField(max_length=255, verbose_name='摘要')
    # 帖子内容
    b_topic_content = models.TextField(verbose_name='帖子内容')
    # 帖子附件
    b_topic_file = models.FileField(upload_to='static/images/', blank=True, verbose_name='附件')
    # 发帖时间
    b_topic_createtime = models.DateTimeField(auto_now_add=datetime.now(), verbose_name='发帖时间')
    # 帖子点击次数
    b_topic_click_num = models.IntegerField(default=0, verbose_name='帖子点击次数')
    # 帖子评论数
    b_topic_comment_num = models.IntegerField(default=0, verbose_name='帖子评论次数')
    # 与标签多对多的关系
    b_topic_tag = models.ManyToManyField(to='B_Tag', through='B_Topic2Tag', verbose_name='外键-标签')
    # 点赞数
    b_topic_up_num = models.IntegerField(default=0, verbose_name='点赞数')
    # 点踩数
    b_topic_down_num = models.IntegerField(default=0, verbose_name='点踩数')

    class Meta:
        # 根据用户ID排序
        ordering = ["b_topic_id"]
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
    def __str__(self):
        return str(self.b_topic_title)


class B_Comment(models.Model):
    '''评论表'''
    # 被评论ID
    b_comment_id = models.AutoField(primary_key=True, verbose_name='评论ID')
    # 评论人名称
    # 评论内容
    b_comment_content = models.CharField(max_length=255, verbose_name='评论内容')
    # 评论时间
    b_comment_create_time = models.DateTimeField(auto_now_add=datetime.now(), verbose_name='评论时间')
    b_comment_user = models.ForeignKey(to='B_User', on_delete=models.DO_NOTHING, verbose_name='用户ID')
    b_comment_topic = models.ForeignKey(to='B_Topic', on_delete=models.DO_NOTHING, verbose_name='帖子ID')
    # b_comment_parent = models.ForeignKey(to='self', null=True, on_delete=models.DO_NOTHING, verbose_name='父ID')

    class Meta:
        # 根据用户ID排序
        ordering = ["b_comment_id"]
        verbose_name = '评论'
        verbose_name_plural = '评论'
    def __str__(self):
        return str(self.b_comment_content)

class B_Integral(models.Model):
    '''积分表'''
    # 默认积分值
    b_integral_num = models.IntegerField(default=-20, verbose_name='积分值')


class B_Tag(models.Model):
    '''标签表'''
    # 标签ID
    b_tag_id = models.AutoField(primary_key=True, verbose_name='标签ID')
    # 标签名
    b_tag_name = models.CharField(max_length=32, verbose_name='标签名')
    # 外键字段--  帖子表
    # b_topic = models.ForeignKey(to='B_Topic', null=False, on_delete=models.DO_NOTHING)

    class Meta:
        # 根据用户ID排序
        ordering = ["b_tag_id"]
        verbose_name = '标签'
        verbose_name_plural = '标签'
    def __str__(self):
        return str(self.b_tag_name)

class B_Up(models.Model):
    '''点赞表'''
    # 0表示踩，1表示赞
    b_is_up = models.BooleanField(verbose_name='是否点赞')
    # 与表B_User一对多关系
    b_up_user = models.ForeignKey(to='B_User', on_delete=models.DO_NOTHING, verbose_name='用户ID')
    # 与表B_Topic一对多关系
    b_up_topic = models.ForeignKey(to='B_Topic', on_delete=models.DO_NOTHING, verbose_name='帖子ID')

