from django.urls import path

from . import views


urlpatterns = [
    path("homework/", views.homework_list),
    path("homework/<int:pk>/", views.homework_retrieve),
    path("endpoints", views.endpoints),
]
