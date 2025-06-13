from django.db import models

# Create your models here.

"""
创建实体类,映射数据库字段
"""
class User(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
