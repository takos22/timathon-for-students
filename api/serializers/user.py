from rest_framework import serializers
from django.contrib.auth.models import User

from ..models import Homework
from .homework import HomeworkSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    homeworks = HomeworkSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "homeworks")
