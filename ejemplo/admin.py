from django.contrib import admin
from ejemplo.models import Film,Genre,Director, FilmReview

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(FilmReview)

