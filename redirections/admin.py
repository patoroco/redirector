from django.contrib import admin

from .models import Redirection


class RedirectionAdmin(admin.ModelAdmin):
    fields = ['path', 'redirection']
    list_display = ('path', 'redirection')


admin.site.register(Redirection, RedirectionAdmin)
