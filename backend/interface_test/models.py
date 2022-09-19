from django.db import models


class TbSubject(models.Model):
    '''学科信息'''
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=1000)
    is_hot = models.BooleanField()
    objects = models.Manager()

    class Meta:
        db_table = 'api_subject'


class TbTeacher(models.Model):
    '''教师信息'''
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
        db_table = 'api_teacher'


class User(models.Model):
    '''用户信息'''
    no = models.AutoField(primary_key=True,verbose_name='编号')
    username = models.CharField(max_length=20,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    tel = models.CharField(max_length=20,verbose_name='手机号')
    reg_date = models.DateTimeField(auto_now_add=True,verbose_name='注册日期')
    last_visit = models.DateTimeField(null=True,verbose_name='最后登录时间')
    token = models.CharField(max_length=200,verbose_name='token信息')
    objects = models.Manager()    #引用object时候不标黄

    class Meta:
        db_table = 'api_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'



