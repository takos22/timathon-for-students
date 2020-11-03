from django.shortcuts import render
from ..models import Homework

def account(request):
    if request.user.is_authenticated:
        homeworks = Homework.objects.filter(user=request.user, finished=False)
    else:
        homeworks = []
    return render(request, "account.html", dict(homeworks=homeworks))
