from django.urls import path
from . import views

app_name = 'bikapi'

urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    # 登陆页
    path('login/', views.login, name='login'),
    # 注册界面
    path('register/', views.register, name='register'),
    # 退出登录
    path('logout/', views.logout, name='logout'),
    # 论坛首页
    path('forum/', views.forum, name='forum'),
    # 标签页
    path('tag/', views.tag, name='tag'),
    # 帖子详情页
    path('topic/<int:id>/', views.topic, name='topic'),
    # 排行榜
    path('top/', views.top, name='top'),
    # 用户首页
    path('userinfo/<int:userid>/', views.userinfo, name='userinfo'),
    # 论坛分区页
    path('zone/', views.zone, name='zone'),
    # 论坛版块页
    path('section/', views.section, name='section'),
    # 发帖
    path('release/', views.release, name='release'),
    # 漫展
    path('topic_comicon/', views.topic_comicon, name='release'),
    # 皮站百科
    path('topic_baike/', views.topic_baike, name='release'),
]