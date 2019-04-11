from django.db import models
from django.urls import path
# Create your models here.

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('test/', views.test, name='test'),
]