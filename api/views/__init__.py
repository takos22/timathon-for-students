from .endpoints import endpoints
from .homework import HomeworkViewSet
from .user import UserViewSet

homework_list = HomeworkViewSet.as_view({"get": "list"})
homework_retrieve = HomeworkViewSet.as_view({"get": "retrieve"})

user_list = UserViewSet.as_view({"get": "list"})
user_retrieve = UserViewSet.as_view({"get": "retrieve"})
