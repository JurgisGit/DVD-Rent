from django.db import models
from django.core.validators import *


class Film(models.Model):
    title = models.CharField('Title', max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField('Year')

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField('Name', max_length=200)
    birth = models.DateField('Date of Birth')
    nationality = models.CharField('Nationality', max_length=200)

    def __str__(self):
        return self.name


class Rating(models.Model):
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=5, help_text='value 1 to 10',
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.film


class Rental(models.Model):
    rented_film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=5, help_text='value 1 to 10',
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    datetime = models.DateField()

    def __str__(self):
        return self.rented_film
