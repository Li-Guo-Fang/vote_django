from django.urls import path
from interface_test import views


urlpatterns = [
    path('login/', views.Login.as_view(http_method_names=['post'])),
    path('subjects/', views.ShowSubjects.as_view()),
    path('teachers/', views.ShowTeacher.as_view()),
    path('praise/', views.PraiseAndCriticize.as_view()),
    path('logout/',views.Logout.as_view()),

]

