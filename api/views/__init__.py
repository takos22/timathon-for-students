from .endpoints import EndpointsViewSet
from .homework import HomeworkViewSet
from .user import UserViewSet
from .login import LoginAPI

endpoints = EndpointsViewSet.as_view({"get": "list"})

homework_list = HomeworkViewSet.as_view({"get": "list"})
homework_retrieve = HomeworkViewSet.as_view({"get": "retrieve"})

user_list = UserViewSet.as_view({"get": "list"})
user_retrieve = UserViewSet.as_view({"get": "retrieve"})

login = LoginAPI.as_view()
