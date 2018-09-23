# coding = utf-8
# 小路由
# 可以访问访问的路由路径
from django.conf.urls import url

# 引入views.py文件，同目录引入用.
from . import views
# 创建路由列表
urlpatterns = [
    url("index", views.dome),
]