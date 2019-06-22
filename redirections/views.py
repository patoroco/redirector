from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect

from .models import Redirection
from .factories import RedirectionFactory

import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('index')


def redirect(request, path):
    host = request.META['HTTP_HOST']
    try:
        redirection = RedirectionFactory.get_with_fallback(
            host=host, path=path)
    except Redirection.DoesNotExist:
        raise Http404(f'Redirection `{host}/{path}` doesn\'t found')

    redirection.views = redirection.views + 1
    redirection.save()

    return HttpResponsePermanentRedirect(redirection.redirection)
