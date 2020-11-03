from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Homework
from ..serializers import HomeworkSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.homeworks.all()

    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
