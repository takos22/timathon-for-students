from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        print("post")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            print("saved")
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            print("auth")
            login(request, user)
            print("login")
            return redirect("index")
    else:
        print("get")
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
