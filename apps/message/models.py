from django.db import models

# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default='', primary_key=True)
    name = models.CharField(max_length=20, verbose_name='用户名', null=True, blank=True, default='')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='联系地址')
    message = models.CharField(max_length=500, verbose_name='留言信息')

    class Meta:
        verbose_name = '用户留言信息'
        verbose_name_plural = verbose_name # 后台显示的信息