from django.http import HttpResponse


def index(request):
    return HttpResponse(f"Índice")


def redirect(request, path):
    return HttpResponse(f"Redirect => {request.META['HTTP_HOST']} - {path}")
