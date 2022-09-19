from functools import wraps
from urllib.parse import quote

import xlwt
from io import BytesIO

from django.db import connections
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from interface_test.Verificate import gen_random_code, Captcha
from polls.models import User, TbTeacher, TbSubject
from polls.serializers import SubjectSerializer, TeacherSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from polls.utils import gen_md5_digest


def is_login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args and args[0].session.get('userid'):
            res = func(*args, **kwargs)
        else:
            return redirect('/polls/login/')
        return res

    return inner


def show_subjects(request):
    '''展示学科信息'''
    subjects = TbSubject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


@is_login
def show_teachers(request):
    '''显示老师信息'''
    sno = int(request.GET.get('sno'))
    # print('-'*20,sno)
    teachers = []
    if sno:
        subject = TbSubject.objects.only('name').get(no=sno)
        teachers = TbTeacher.objects.filter(no=subject.no).order_by('no')
    return render(request, 'teachers.html', {
        'subject': subject,
        'teachers': teachers
    })


# @api_view(('GET',))
# def show_subjects(request):
#     # print(request.method,request.get_full_path(),request.COOKIES,request.content_type)
#     subjects = TbSubject.objects.all().order_by('no')
#     serializer = SubjectSerializer(subjects,many=True)
#     return Response(serializer.data)
#
#
# @api_view(('GET',))
# def show_teachers(request):
#     try:
#         sno = int(request.GET.get('sno'))
#         subject = TbSubject.objects.only('name').get(no=sno)
#         teachers = TbTeacher.objects.filter(no=subject.no).order_by('no')
#         subject_serializer = SubjectSerializer(subject)
#         teachers_serializer = TeacherSerializer(teachers,many=True)
#         return Response({'subject':subject_serializer.data,'teachers':teachers_serializer.data})
#     except (ValueError,TypeError,TbSubject.DoesNotExist):
#         return Response(status=404)


def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'GET':
        # 记住来源的url，如果没有则设置为首页('/')
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/polls/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                # return redirect('/polls/')  # polls前加/是绝对路径，如果不加就是相对路径，login后面拼接
                # 重定向到来源的url
                return HttpResponseRedirect(request.session['login_from'])
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint': hint})


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/polls/')


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    '''投票'''
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = TbTeacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.gcount += 1
                count = teacher.gcount
            else:
                teacher.bcount -= 1
                count = teacher.bcount
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, TbTeacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)


def export_teachers_excel(request):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet('老师信息表')
    # 查询所有老师的信息
    queryset = TbTeacher.objects.all()
    # 向Excel表单中写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name, )
    # 向单元格中写入老师的数据
    props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, TbSubject):
                value = value.name
            sheet.write(row + 1, col, value)
    # 保存Excel
    buffer = BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename = quote('老师.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment; filename*=utf-8\'\'{filename}'
    return resp


def get_charts_data(requst):
    '''获取统计图表JSON数据'''
    names = []
    totals = []
    with connections['backend'].cursor() as cursor:
        cursor.execute('select dname,total from vm_dept_emp')
        for row in cursor.fetchall():
            names.append(row[0])
            totals.append(row[1])
    return JsonResponse({'name': names, 'totals': totals})


def get_teachers_data(request):
    queryset = TbTeacher.objects.all()
    names = [teacher.name for teacher in queryset]
    good_counts = [teacher.gcount for teacher in queryset]
    bad_counts = [teacher.bcount for teacher in queryset]
    # return JsonResponse({'names': names, 'good': good_counts, 'bad': bad_counts})
    return render(request, 'teachers_data.html', {
        'names': names,
        'good': good_counts,
        'bad': bad_counts
    })
