from .endpoints import endpoints
from .homework import HomeworkViewSet

homework_list = HomeworkViewSet.as_view({"get": "list"})
homework_retrieve = HomeworkViewSet.as_view({"get": "retrieve"})
