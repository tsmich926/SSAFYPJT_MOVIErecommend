from rest_framework import serializers
from movies.models import Movie,Actor,Director,Genre,Review,Comment
# from django.conf import settings
from django.contrib.auth import get_user_model
# from movies.serializers import MovieSerializer, ActorSerializer, DirectorSerializer, GenreSerializer
# from movies.serializers import 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  get_user_model()
        fields = '__all__'

class MS(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields='__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class AS(serializers.ModelSerializer):
        class Meta:
            model=Actor
            fields='__all__'
    class GS(serializers.ModelSerializer):
        class Meta:
            model=Genre
            fields='__all__'
    class DS(serializers.ModelSerializer):
        class Meta:
            model=Director
            fields='__all__'
    
    class RS(serializers.ModelSerializer):
        movie = MS(read_only=True)
        user = UserSerializer(read_only=True)
        likes=UserSerializer(many=True,read_only=True)
        class Meta:
            model=Review
            fields='__all__'
            read_only_fields=('movie','user')
    like_reviews =RS(many=True,read_only=True)
    my_reviews=RS(many=True,read_only=True)
    movies=MS(many=True,read_only=True)
    actors=AS(many=True,read_only=True)
    directors=DS(many=True,read_only=True)
    genres=GS(many=True,read_only=True)
    followings=UserSerializer(many=True,read_only=True)
    followers=UserSerializer(many=True,read_only=True)
    class Meta:
        model =  get_user_model()
        fields = '__all__'



