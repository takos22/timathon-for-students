from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("homework/", views.homework, name="homework"),
    path("account/", views.account, name="account"),
    path("account/login/", views.login, name="login"),
    path("account/signup/", views.signup, name="signup"),
    path("account/logout/", views.logout, name="logout"),
    # path("contact/", views.contact, name="contact"),
]
