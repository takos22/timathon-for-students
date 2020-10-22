from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("homework/", views.index, name="homework"),
    path("account/", views.index, name="account"),
    path("contact/", views.index, name="contact"),
]
