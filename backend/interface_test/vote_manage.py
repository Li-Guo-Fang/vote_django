import operator
from django.http import JsonResponse
from interface_test.models import User, TbSubject, TbTeacher
from polls.utils import gen_md5_digest, get_jwt_token

# api_views,check_params一个类，后面do_ 可以再封装一个类
param_dict = {'login': ['username', 'password'],
              'show_teacher': ['sno'],
              'praise_and_criticize': ['tno', 'is_good'],
              'logout': ['uid'],
              }


def check_params(api, data):
    return operator.eq(param_dict.get(api), list(data.keys()))



def api_views(api, data, func):
    if check_params(api, data):
        try:
            res = func(data)
            return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': str(e)})
    return JsonResponse({'code': '500', 'msg': '参数信息错误'}, json_dumps_params={'ensure_ascii': False})


def do_login(data):
    username = data.get('username')
    password = data.get('password')
    password = gen_md5_digest(password)
    user = User.objects.filter(username=username, password=password).first()
    if user:
        token = get_jwt_token(username)
        user.token = token
        user.save()
        return {'code': '200', 'msg': '登陆成功', 'data': {'token': token}}
    return {'code': '401', 'msg': '用户名或密码错误'}


def do_show_Subject():
    subjects = TbSubject.objects.all().order_by('no')
    subjects = [subject.name for subject in subjects]
    return JsonResponse({'code': 200, 'data': {'subjects': subjects}}, json_dumps_params={'ensure_ascii': False})


def do_show_teacher(data):
    sno = int(data.get('sno'))
    subject = TbSubject.objects.only('name').get(no=sno)  # 需要判断没有sno时的处理
    teachers = TbTeacher.objects.filter(no=subject.no).order_by('no')
    teachers = [teacher.name for teacher in teachers]
    return {'code': 200, 'data': {'teachers': teachers}}


def do_praise_and_criticize(data):
    tno = int(data.get('tno'))
    is_good = int(data.get('is_good'))  # 1:好评；0：差评
    teacher = TbTeacher.objects.get(no=tno)
    if is_good:
        teacher.gcount += 1
        count = teacher.gcount
    else:
        teacher.bcount += 1
        count = teacher.bcount
    teacher.save()
    return {'code': '200', 'msg': '投票成功', 'count': count}


def do_logout(data):
    user_id = int(data.get('uid'))
    user = User.objects.filter(no=user_id).first()
    user.token = ''
    user.save()
    return {'code': '200', 'msg': '注销成功'}
