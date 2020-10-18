from rest_framework import serializers

from ..models import Homework


class HomeworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homework
        fields = ("id", "subject", "name", "description", "added_date", "due_date", "finished")
