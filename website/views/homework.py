from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from ..models import Homework


def homework(request):
    if not request.user.is_authenticated:
        return redirect("login")
    homeworks = request.user.homeworks.all()
    token = Token.objects.get_or_create(user=request.user)[0].key
    return render(request, "homework.html", dict(homeworks=homeworks, token=token))
