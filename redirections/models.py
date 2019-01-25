from django.db import models


class Redirection(models.Model):
    path = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
