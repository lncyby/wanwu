from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Adver(models.Model):
    orderID = models.IntegerField()
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length = 600)
