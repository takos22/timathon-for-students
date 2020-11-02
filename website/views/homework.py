from django.shortcuts import redirect, render
from ..models import Homework


def homework(request):
    if not request.user.is_authenticated:
        return redirect("login")
    homeworks = request.user.homeworks.all()
    return render(request, "homework.html", dict(homeworks=homeworks))
