from django.urls import path, include

from . import views


urlpatterns = [
    # Anyone
    path("endpoints", views.endpoints, name="endpoints"),
    path("login", views.login, name="login"),
    path("auth/", include("rest_framework.urls"), name="rest-framework-auth"),

    # Authentificated
    path("homework/", views.homework_list, name="homework-list"),
    path("homework/<int:pk>/", views.homework_retrieve, name="homework-retrieve"),

    # Admin
    path("user/", views.user_list, name="user-list"),
    path("user/<int:pk>/", views.user_retrieve, name="user-retrieve"),
]
