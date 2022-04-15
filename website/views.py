from django.shortcuts import render
# Create your views here.
import re
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("kavehmollaei")

def json_response(request):
    return JsonResponse({'name':'kaveh'})

def about(request):
    return HttpResponse('I am kaveh molaei and we developer')    

def index(request):
    return HttpResponse('<h1> ths is index page<h2>')