from django.urls import path,re_path
from  website.views import about, http_test,json_response,index,contact,template,blog,portfolio



urlpatterns = [
path('blog/',http_test),
path('blog/json/',json_response),
path('',index),
path('about/' ,about),
path('blogfa/',blog),
path('portfolio',portfolio),
# re_path(r'^[a-c]/',about),
path('contact/',contact),
path('template/',template),
]
