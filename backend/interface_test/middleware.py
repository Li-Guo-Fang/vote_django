import re

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from interface_test.models import User
from polls.utils import decode_jwt_token


class LoginCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pattern = r'^(/polls/.*|/api/login/|/$)'
        match = re.search(pattern, request.path)
        if match:
            return
        msg = 'token信息有误 '
        try:
            token = request.META.get('HTTP_AUTHORIZATION',None).replace('Bearer ', '')  # 'Bearer '：postman的语法，其他接口工具可能有变动
            token_test = decode_jwt_token(token)  # 解码
            username = token_test['data']['username']
            user = User.objects.filter(username=username).first()
            if token == user.token:
                return
        except Exception as e:
            msg += str(e)
        return JsonResponse({'code': '401', 'msg': msg}, json_dumps_params={'ensure_ascii': False})

    # def process_response(self,request,response):
        # print(response._container)
        #[b'{"code": "200", "msg": "\xe7\x99", "data": {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE5NzQxMzMwODEsImlhdCI6MTY2MzA5MzA4MSwiZGF0YSI6eyJ1c2VybmFtZSI6InRlc3QiLCJyb2xlX2RhdGEiOiJkZWZhdWx0In19.xtT2Q8qgXMb66R71iEhNJoxL3auRS3v3GutbWGOw6Yw"}}']
        #response._container中数值进行判断
        # return response