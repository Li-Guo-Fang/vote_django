# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbSubject(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=1000)
    is_hot = models.BooleanField()
    objects = models.Manager()

    class Meta:
        db_table = 'tb_subject'


class TbTeacher(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)
    birth = models.DateField()
    intro = models.CharField(max_length=1000)
    photo = models.ImageField(max_length=255)
    gcount = models.IntegerField()
    bcount = models.IntegerField()
    sno = models.ForeignKey(TbSubject, models.DO_NOTHING, db_column='sno')
    objects = models.Manager()

    class Meta:
        db_table = 'tb_teacher'


class User(models.Model):
    '''用户'''
    no = models.AutoField(primary_key=True,verbose_name='编号')
    username = models.CharField(max_length=20,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    tel = models.CharField(max_length=20,verbose_name='手机号')
    reg_date = models.DateTimeField(auto_now_add=True,verbose_name='注册日期')
    last_visit = models.DateTimeField(null=True,verbose_name='最后登录时间')
    objects = models.Manager()

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'















