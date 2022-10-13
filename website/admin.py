from django.contrib import admin
from .models import Film, Director, Rating, Rentals


admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Rating)
admin.site.register(Rentals)
