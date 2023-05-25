from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Actor, Director, Genre, Movie, Review, Rating, Comment

# Register your models here.
# Register your models here.

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Comment)