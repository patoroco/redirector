from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Redirection
import re


def index(request):
    return HttpResponse(f"Índice")


def redirect(request, path):
    regexp = re.compile('.*TelegramBot.*')
    if regexp.search(request.META['HTTP_USER_AGENT']):
        return HttpResponse('Ocultando a Telegram')

    redirection = get_object_or_404(Redirection, path=path)
    return HttpResponsePermanentRedirect(redirection.redirection)
