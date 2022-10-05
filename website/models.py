from django.db import models

class Film(models.Model):
    title = models.CharField('Title', max_length=200)
    director = models.CharField('Director', max_length=200)
    year = models.IntegerField('Year')