from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
# Create your models here.
class Actor(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    profile_path=models.TextField(null=True)
    gender=models.IntegerField()

class Director(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    profile_path=models.TextField(null=True)

class Genre(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)


class Movie(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    title=models.CharField(max_length=100)
    overview=models.TextField()
    release_date=models.DateField(null=True)
    poster_path=models.TextField()
    vote_average=models.IntegerField()
    popularity=models.IntegerField()

    actors=models.ManyToManyField(Actor, related_name='movies')
    directors=models.ManyToManyField(Director, related_name='movies')
    genres=models.ManyToManyField(Genre, related_name='movies')



class Review(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_reviews')  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Ratings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
