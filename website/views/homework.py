from django.shortcuts import render
from ..models import Homework


def homework(request):
    homeworks = request.user.homeworks.all()
    return render(request, "homework.html", dict(homeworks=homeworks))
