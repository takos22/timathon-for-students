from rest_framework import serializers

from ..models import Homework


class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Homework
        fields = ("id", "user", "subject", "name", "description", "added_date", "due_date", "finished")
