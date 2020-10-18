from django.http import JsonResponse

def endpoints(request):
    return JsonResponse({"endpoints": ["homework"]})
