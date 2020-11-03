from django.urls import path, include

from . import views


urlpatterns = [
    # Anyone
    path("endpoints/", views.endpoints, name="api.endpoints"),
    path("login/", views.login, name="api.login"),

    # Authentificated
    path("homework/", views.homework_list, name="api.homework-list"),
    path("homework/<int:pk>/", views.homework_retrieve, name="api.homework-retrieve"),

    # Admin
    path("user/", views.user_list, name="api.user-list"),
    path("user/<int:pk>/", views.user_retrieve, name="api.user-retrieve"),
]
