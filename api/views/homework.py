from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Homework
from ..serializers import HomeworkSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.homeworks.all()
