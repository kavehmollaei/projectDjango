from django.shortcuts import render
# Create your views here.
import re
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("kavehmollaei")

def json_response(request):
    return JsonResponse({'name':'kaveh'})

def about(request):
    return render(request,'about.html')    

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')