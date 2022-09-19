import re
from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # | 分隔要匹配的多个url，从左到右匹配，有匹配就返回匹配值，否则返回None。
        # pattern = r'^(/$|/user/user/[0-9]+/$|/user/user/$|/user/getuserall|/user/get_token_code|/user/update_phone_no|/stock|/future)'
        pattern = r'^/polls/teachers/.*'

        # 如果 request.path 的开始位置能够找到这个正则样式的任意个匹配，就返回一个相应的匹配对象。
        # 如果不匹配，就返回None
        match = re.search(pattern, request.path)
        # 需要拦截的url
        print('------',request.user)
        if match and not request.user.is_authenticated:
            print('用户未登录URL拦截 >>: ', request.path)
            # 主页未登录
            # if request.path == '/polls/':
            return HttpResponseRedirect('/polls/login/')
                # ajax请求未登录
            # else:
            #     return JsonResponse({'status': False, 'info': '用户未登录!'},json_dumps_params={'ensure_ascii':False})
