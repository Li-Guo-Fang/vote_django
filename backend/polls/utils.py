import hashlib
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from functools import wraps

from django.http import JsonResponse


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


def get_jwt_token(user_name, role_data='default'):
    # token加密
    payload = {
        'exp': datetime.utcnow() + timedelta(settings.TOKEN_TIMEOUT),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': user_name, 'role_data': role_data}
    }
    encoded_jwt = jwt.encode(payload, 'secret_key', algorithm='HS256')
    return encoded_jwt.decode('utf-8')


def decode_jwt_token(encoded_jwt):
    # token解密
    de_code = jwt.decode(encoded_jwt, 'secret_key', algorithms=['HS256'])
    return de_code


def is_login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args and args[0].META.get('HTTP_AUTHORIZATION'):
            token = args[0].META.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
            token_test = decode_jwt_token(token)  # 解码
            username = token_test['data']['username']
            if username:
                res = func(*args, **kwargs)
                return res
        return JsonResponse({'code': '401', 'msg': 'token信息无效'}, json_dumps_params={'ensure_ascii': False})

    return inner


if __name__ == '__main__':
    token = get_jwt_token('lisi')
    print(decode_jwt_token(token))
