from rest_framework import viewsets

from ..models import Homework
from ..serializers import HomeworkSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all().order_by("id")
    serializer_class = HomeworkSerializer
