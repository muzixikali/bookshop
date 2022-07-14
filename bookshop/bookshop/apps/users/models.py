from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    """用户模型类"""
    phone = models.CharField(max_length=20, unique=True, verbose_name="电话号码")

    class Meta:
        db_table = 'users_info'  # 自定义表名
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.username} {self.email}"
