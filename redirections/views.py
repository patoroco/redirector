from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from .models import Redirection


def index(request):
    return HttpResponse('index')


def redirect(request, path):
    host = request.META['HTTP_HOST']
    try:
        redirection = Redirection.objects.get(host=host, path=path)
    except Redirection.DoesNotExist:
        try:
            redirection = Redirection.objects.get(host=host, path='default')
        except Redirection.DoesNotExist:
            raise Http404('Redirection doesn\'t found')

    redirection.views = redirection.views + 1
    redirection.save()

    return HttpResponsePermanentRedirect(redirection.redirection)
