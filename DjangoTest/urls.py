"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 引入views.py文件
# from app import views
# 引入小路由包
from django.conf.urls import include

# 路由列表
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('名字', views.dome()),
    # 直接映射视图函数
    # path('demo', views.dome),
    # 小路由映射大路由
    path("", include("app.urls")),
]


