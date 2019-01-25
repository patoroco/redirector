from django.urls import path, re_path

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    re_path(r'(.*)', views.redirect, name='redirect'),
]
