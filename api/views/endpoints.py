from django.http import JsonResponse


def endpoints(request):
    return JsonResponse(
        {
            "endpoints": {
                "endpoints": "Get all the endpoints of the API.",
                "homework": "Get a list of all the user's homeworks.",
                "homework/<int:pk>": "Get a user's homework by its id.",
            }
        }
    )
