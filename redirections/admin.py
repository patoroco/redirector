from django.contrib import admin

from .models import Redirection


class RedirectionAdmin(admin.ModelAdmin):
    fields = ['path', 'redirection']
    list_display = ('host', 'path', 'redirection', 'pub_date')

    def save_model(self, request, obj, form, change):
        obj.host = request.META['HTTP_HOST']
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(host=request.META['HTTP_HOST'])


admin.site.register(Redirection, RedirectionAdmin)
