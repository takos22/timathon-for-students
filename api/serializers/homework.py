from rest_framework import serializers

from ..models import Homework

from .user import UserSerializer


class HomeworkSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Homework
        fields = ("id", "user", "subject", "name", "description", "added_date", "due_date", "finished")
