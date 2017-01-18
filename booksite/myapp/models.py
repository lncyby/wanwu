from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()

class User(AbstractUser):
    avater = models.ImageField(default = 'static/default.png',max_length =
            200,blank = True,null = True,verbose_name="Head_portrait")
    mobile = models.CharField(max_length = 11,blank = True,null =
            True,verbose_name = 'tel')
    class Meta:
        verbose_name = 'User'
        ordering = ['-id']

    def __unicode__(self):
        return self.username

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
        verbose_name = "Publisher"
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
#    sex = models.CharField(blank = True,max_length = 5)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')
    def __unicode__(self):
        return u"%s %s"%(self.first_name,self.last_name)
    class Meta:
        verbose_name = "Author"
        ordering = ['first_name']

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)
    publisher = models.ForeignKey(Publisher,related_name = 'books')
    author = models.ManyToManyField(Author)
    objects = BookManager()
    #myobjects = BookManager()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "Book"
        ordering = ['id']

