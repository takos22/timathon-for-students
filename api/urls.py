from django.urls import path

from . import views


urlpatterns = [
    path("homework", views.homework),
    path("endpoints", views.endpoints),
]
