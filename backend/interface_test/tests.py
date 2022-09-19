from django.test import TestCase

# Create your tests here.
import operator

param_dict = {'login': ['username', 'password']}
data = {'username':'','password':''}

def check_params(api,data):
    return operator.eq(param_dict.get(api),list(data.keys()))


print(check_params('login', data))