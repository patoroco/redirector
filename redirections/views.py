from django.shortcuts import get_object_or_404, render
from django.http import HttpResponsePermanentRedirect
from .models import Redirection


def redirect(request, path):
    redirection = get_object_or_404(
        Redirection,
        host=request.META['HTTP_HOST'],
        path=path
    )
    return HttpResponsePermanentRedirect(redirection.redirection)
