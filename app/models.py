# coding = utf-8
from django.db import models

# Create your models here.
# 创建数据模型
class MyModels(models.Model):
    username = models.CharField(max_length=50)

    class Meta:
        db_table = "mytable"