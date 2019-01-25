from django.db import models


class Redirection(models.Model):
    host = models.CharField(max_length=100)
    path = models.CharField(max_length=200, blank=True)
    redirection = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    # Únicos
    class Meta:
        unique_together = ('host', 'path')
