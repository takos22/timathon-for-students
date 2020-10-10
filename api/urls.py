from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("homework", views.HomeworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("endpoints", views.endpoints),
]
