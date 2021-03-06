from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    company = models.CharField(max_length=32, verbose_name="单位,集团下属机构名字")
    address = models.TextField(verbose_name="所在地")

class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)  ### 与django维护的user模型建立一对一的关系
    name = models.CharField(max_length=32, verbose_name='中文名')
    QQ = models.CharField(max_length=32, verbose_name='QQ号')
    phone = models.CharField(max_length=32, verbose_name='手机号')
    # company = models.CharField(max_length=32, verbose_name="单位,集团下属机构名字")
    company = models.ForeignKey(to=Company,on_delete=models.CASCADE)

