from rest_framework import serializers
from .models import Movie,Actor,Review


class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields=('title',)
            # read_only_fields=('actors_settt',)
    movies=MovieSerializer(many=True,read_only=True)
    class Meta:
        model=Actor
        fields='__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors=ActorSerializer(many=True,read_only=True)
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)
        

class MovieDetailSerializer(serializers.ModelSerializer):
    class ReviewS(serializers.ModelSerializer):
        class Meta:
            model=Review
            fields=('title','content')
    
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)
    actors=ActorSerializer(many=True,read_only=True)
    review_count=serializers.IntegerField(source='review_set.count',read_only=True)
    review_set=ReviewS(many=True,read_only=True)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=('movie',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields=('title',)
    movie=MovieSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'