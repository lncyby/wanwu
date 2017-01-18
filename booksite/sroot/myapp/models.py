from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Chubanshe"
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
#    sex = models.CharField(blank = True,max_length = 5)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)

