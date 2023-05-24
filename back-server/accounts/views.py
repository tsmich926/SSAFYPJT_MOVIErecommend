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
from .serializers import UserSerializer,UserDetailSerializer
from movies.serializers import MovieDetailSerializer

#####


# user detail
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_detail(request,user_pk):
#     User=get_user_model()    
#     person=User.objects.get(pk=user_pk)


# 팔로우, detail
@api_view(['POST','GET','PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request,user_pk):
    User=get_user_model()
    person=User.objects.get(pk=user_pk)
    print(person)
    if request.method=='PUT':
        serializer=UserDetailSerializer(person,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='POST':
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        serializer=UserDetailSerializer(person)
        return Response(serializer.data)
    if request.method=='GET':
        serializer=UserDetailSerializer(person)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_user(request):
    User=get_user_model()
    person=User.objects.get(pk=request.user.pk)
    serializer=UserDetailSerializer(person)
    return Response(serializer.data)