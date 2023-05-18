from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie,Review,Actor
from .serializers import MovieSerializer,ActorSerializer,ReviewSerializer,MovieDetailSerializer,ActorDetailSerializer,ReviewDetailSerializer
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors=Actor.objects.all()
    serializer=ActorSerializer(actors,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request,actor_pk):
    actor=get_object_or_404(Actor,pk=actor_pk)
    serializer=ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    serializer=MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews=Review.objects.all()
    serializer=ReviewSerializer(reviews,many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)

    if request.method=='GET':
        serializer=ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



################
## reveiw 디테일

# @api_view(['GET', 'DELETE', 'PUT'])
# def review_detail(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     review = get_object_or_404(Review, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)