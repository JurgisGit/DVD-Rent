from django.contrib import admin
from .models import Film, Director, Rating, Rental


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality')


class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'rented_film')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'rating')


admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Rental, RentalAdmin)
