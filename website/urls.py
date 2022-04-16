from django.urls import path
from  website.views import about, http_test,json_response,index



urlpatterns = [
path('blog/',http_test),
path('blog/json/',json_response),
path('',index),
path('about/',about)
