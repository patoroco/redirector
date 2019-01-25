from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Redirection
import re


def index(request):
    return HttpResponse(f"Índice")


def redirect(request, path):
    # regexp = re.compile('.*TelegramBot.*')
    # if regexp.search(request.META['HTTP_USER_AGENT']):
    #     return HttpResponse('<title>Ocultando a Telegram</title>')

    redirection = get_object_or_404(
        Redirection,
        host=request.META['HTTP_HOST'],
        path=path
    )
    return HttpResponsePermanentRedirect(redirection.redirection)
