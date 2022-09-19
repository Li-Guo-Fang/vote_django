from django.views import View
from interface_test.vote_manage import do_login, do_show_teacher, do_praise_and_criticize, api_views, do_logout,do_show_Subject


class Login(View):
    def post(self, request):
        data = request.POST.dict()
        res = api_views('login', data, do_login)
        return res


class ShowSubjects(View):
    def get(self,request):
        res = do_show_Subject()
        return res


class ShowTeacher(View):
    def get(self, request):
        data = request.GET.dict()
        res = api_views('show_teacher', data, do_show_teacher)
        return res


class PraiseAndCriticize(View):
    def get(self, request):
        data = request.GET.dict()
        res = api_views('praise_and_criticize', data, do_praise_and_criticize)
        return res


class Logout(View):
    def post(self,request):
        data = request.POST.dict()
        res = api_views('logout', data, do_logout)
        return res

