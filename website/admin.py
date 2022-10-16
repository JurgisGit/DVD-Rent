from django.contrib import admin
from .models import Film, Director, Rating, Rental


admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Rating)
admin.site.register(Rental)
