
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index),    
    path('author', csrf_exempt(views.author)),    
    path('book', csrf_exempt(views.book)),    
]