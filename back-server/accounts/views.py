from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie,Review,Actor,Director,Genre,Rating,Comment
from .serializers import UserSerializer
from movies.serializers import MovieDetailSerializer

#####


# user detail
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_detail(request,user_pk):
#     User=get_user_model()    
#     person=User.objects.get(pk=user_pk)


# 팔로우, detail
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_detail(request,user_pk):
    User=get_user_model()
    person=User.objects.get(pk=user_pk)
    if request.method=='POST':
        if person != request.user:
            if person.follower.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        serializer=UserSerializer(person)
        return Response(serializer.data)
    if request.method=='GET':
        serializer=UserSerializer(person)
        return Response(serializer.data)
    
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def my_user(request):
    User=get_user_model()
    person=User.objects.get(pk=request.user.pk)
    serializer=UserSerializer(person)
    return Response(serializer.data)