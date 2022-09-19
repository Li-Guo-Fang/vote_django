from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('', views.show_subjects),
    path('teachers/', views.show_teachers),
    path('praise/', views.praise_or_criticize),
    path('teachers_data/',views.get_teachers_data),
    path('excel/', views.export_teachers_excel),
    path('admin/', admin.site.urls),
    path('logout/',views.logout),

]

