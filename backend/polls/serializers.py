from rest_framework import serializers
from polls.models import TbTeacher, TbSubject


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbSubject
        # fields = '__all__'
        fields = ('no','name')

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbTeacher
        exclude = ('sno',)
        # fields = '__all__'
