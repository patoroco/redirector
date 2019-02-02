from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Redirection


def index(request):
    return HttpResponse('index')


def redirect(request, path):
    redirection = get_object_or_404(
        Redirection,
        host=request.META['HTTP_HOST'],
        path=path
    )
    return HttpResponsePermanentRedirect(redirection.redirection)
