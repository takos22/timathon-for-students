from django import http
from rest_framework import viewsets
from rest_framework.response import Response


class EndpointsViewSet(viewsets.GenericViewSet):
    def list(self, request):
        return Response(
            {
                "endpoints": {
                    "endpoints": "Get all the endpoints of the API.",
                    "auth/login": "Log into the API.",
                    "auth/logout": "Log out of the API.",
                    "user": "Get a list with only your user (or all the users if you're admin).",
                    "user/<int:pk>": "Get a user by its id (pretty much useless if you're not admin).",
                    "homework": "Get a list of all the user's homeworks.",
                    "homework/<int:pk>": "Get a user's homework by its id.",
                }
            }
        )
