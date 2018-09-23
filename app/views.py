# coding = utf-8
from django.shortcuts import render

# Create your views here.

# 引入HTTP协议
from django.http import HttpResponse
# 引入数据模型
from .models import MyModels
# 定义视图函数

def dome(request):
    # html = "<html><head>河北</head><body><h3>唐山</h3></body></html>"
    # 返回字符串
    # return HttpResponse(html)
    # 判断请求方式
    if request.method == "POST":
        username = request.POST["username"]
        m = MyModels(username=username)
        # 保存到数据库
        m.save()

    user_list_obj = MyModels.objects.all()

    # 返回一个页面
    return render(request, "index.html", {'order':user_list_obj})
