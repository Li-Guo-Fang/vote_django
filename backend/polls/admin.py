from django.contrib import admin

from polls.models import TbSubject, TbTeacher


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'intro','gcount', 'bcount', 'sno')
    search_fields = ('name',)
    ordering = ('no',)


admin.site.register(TbSubject, SubjectModelAdmin)
admin.site.register(TbTeacher, TeacherModelAdmin)