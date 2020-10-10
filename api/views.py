from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HomeworkSerializer
from .models import Homework


# Create your views here.


def endpoints(request):
    return JsonResponse({"Endpoints": ["get_homework_by_id"]})


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all().order_by("id")
    serializer_class = HomeworkSerializer
