from django.urls import path 
from.views impor home,about
uripatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),\
]