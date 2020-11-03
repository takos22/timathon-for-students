from django.shortcuts import redirect, render
from ..models import Homework


def homework(request):
    if not request.user.is_authenticated:
        return redirect("login")
    homeworks = request.user.homeworks.all()
    token = request.session["token"]
    return render(request, "homework.html", dict(homeworks=homeworks, token=token))
