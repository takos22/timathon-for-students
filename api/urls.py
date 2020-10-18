from django.urls import path

from . import views


urlpatterns = [
    path("endpoints", views.endpoints),
    path("homework/", views.homework_list),
    path("homework/<int:pk>/", views.homework_retrieve),
    path("user/", views.user_list),
    path("user/<int:pk>/", views.user_retrieve),
]
