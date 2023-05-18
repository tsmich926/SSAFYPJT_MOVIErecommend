from rest_framework import serializers
# from .models import Movie,Actor,Director,Genre,Review,Ratings,Comment
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'