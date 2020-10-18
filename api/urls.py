from django.urls import path

from . import views


urlpatterns = [
    # Anyone
    path("endpoints", views.endpoints, name="endpoints"),

    # Authentificated
    path("homework/", views.homework_list),
    path("homework/<int:pk>/", views.homework_retrieve),

    # Admin
    path("user/", views.user_list),
    path("user/<int:pk>/", views.user_retrieve),
]
