from turtle import title
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime # 追加

# Create your models here.
class SredModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(verbose_name='掲示板作成日時',default=localtime(timezone.now()))
    updated_at = models.DateTimeField(verbose_name='編集日時',blank=True,null=True)   
    delete_flg = models.BooleanField(help_text='削除されたらTrue',verbose_name='掲示板削除フラグ',default=False)
    # (null=True,blank=True)は空のデータベースが使える

    def __str__(self):
        return self.title


class Sred_msg_post(models.Model):
    # msg_post_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='メッセージ作成者')
    sred = models.ForeignKey(SredModel, on_delete=models.CASCADE)
    msg_detail = models.CharField(max_length=255,verbose_name='メッセージ内容')
    msg_author = models.CharField(max_length=50)
    create_at = models.DateTimeField(verbose_name='メッセージ送信日時',default=localtime(timezone.now()))
    delete_flg = models.BooleanField(help_text='削除されたらTrue',verbose_name='メッセージ削除フラグ',default=False)
    def __str__(self):
        return self.msg_detail