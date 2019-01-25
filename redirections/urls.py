from django.urls import path, re_path
from django.views.generic import View

from . import views

urlpatterns = [
    path('loaderio-700a3036a753553143eacb48bbbf9684.html',
         views.loader_io, name='loader'),
    path('index.html', views.index, name='index'),
    re_path(r'(.*)', views.redirect, name='redirect'),
]
