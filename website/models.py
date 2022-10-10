from django.db import models
from django.core.validators import *


class Film(models.Model):
    title = models.CharField('Title', max_length=200)
    director = models.CharField('Director', max_length=200)
    year = models.IntegerField('Year')


class Director(models.Model):
    name = models.CharField('Name', max_length=200)
    birth = models.DateField('Date of Birth')
    nationality = models.CharField('Nationality', max_length=200)


class Rating(models.Model):
    film = models.CharField('Film', max_length=250)
    year = models.IntegerField('Year')
    director = models.CharField('Director', max_length=250)
    rating = models.IntegerField(default=5, help_text='value 1 to 10', validators=[MaxValueValidator(10), MinValueValidator(1)])