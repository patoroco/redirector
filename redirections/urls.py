from django.urls import path, re_path
from django.views.generic import View

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    re_path(r'(.*)', views.redirect, name='redirect'),
]
