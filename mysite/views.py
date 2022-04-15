import re
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("kavehmollaei")

def json_response(request):
    return JsonResponse({'name':'kaveh'})    