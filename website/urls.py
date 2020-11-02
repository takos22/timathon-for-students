from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("homework/", views.homework, name="homework"),
    path("account/", views.account, name="account"),
    path("account/login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("account/signup/", views.signup, name="signup"),
    path("account/logout/", views.logout, name="logout"),
    # path("contact/", views.contact, name="contact"),
]
