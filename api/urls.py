from django.urls import include, path

from . import views


urlpatterns = [
    path("homework", views.homework),
    path("endpoints", views.endpoints),
]
