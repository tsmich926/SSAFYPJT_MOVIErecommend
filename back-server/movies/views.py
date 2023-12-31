from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Movie,Review,Actor,Director,Genre,Rating,Comment
from .serializers import (ActorSerializer,MovieSerializer,ReviewSerializer,MovieDetailSerializer,
                          ActorDetailSerializer,ReviewDetailSerializer,MovieSearchSerializer,
                         DirectorDetailSerializer, DirectorSerializer, GenreSerializer,GenreDetailSerializer,
                         CommentSerializer,RatingSerializer )
# Create your views here.
import random
from datetime import date


# 영화 전체 리스트를 요청하는 것.
#
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def movie_list(request):
    print(request.GET)
    page=int(request.GET.get('page'))
    movies=Movie.objects.all()[page*100:(page+1)*100]
    # movies=get_list_or_404(Movie)
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

# 영화를 제목으로 검색
#
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def movie_title_search_detail(request,movie_title):
    movies=Movie.objects.filter(title__contains=movie_title) 
    if not movies.exists():
    # 조건에 맞는 데이터가 없는 경우 빈 데이터를 반환하도록 처리
        movies_data = []
    else:
    # movies를 serializer를 사용하여 직렬화
        serializer = MovieSearchSerializer(movies, many=True)
        movies_data = serializer.data
    return Response(movies_data)

# 무비 디테일 (리뷰, 배우, 감독, 포함), post 시 좋아요 method
@permission_classes([IsAuthenticated])
@api_view(['POST','GET'])
def movie_detail(request,movie_pk):
    movie=get_object_or_404(Movie,id=movie_pk)
    if request.method=='POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
    serializer=MovieDetailSerializer(movie)
    return Response(serializer.data)


# 전체 배우리스트 요청 (이름, 사진)
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def actor_list(request):
    # actors=Actor.objects.all()[:100]
    page=int(request.GET.get('page'))
    actors=get_list_or_404(Actor)[page*100:(page+1)*100]
    serializer=ActorSerializer(actors,many=True)
    return Response(serializer.data)


# 배우 detail
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def actor_detail(request,actor_pk):
    actor=get_object_or_404(Actor,pk=actor_pk)
    if request.method=='POST':
        if actor.like_users.filter(pk=request.user.pk).exists():
            actor.like_users.remove(request.user)
        else:
            actor.like_users.add(request.user)
    serializer=ActorDetailSerializer(actor)
    return Response(serializer.data)

# 전체 감독리스트 요청 (이름, 사진)
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def director_list(request):
    page=int(request.GET.get('page'))
    directors=get_list_or_404(Director)[page*100:(page+1)*100]
    serializer=DirectorSerializer(directors,many=True)
    return Response(serializer.data)


# 감독 detail, 좋아요
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def director_detail(request,director_pk):
    director=get_object_or_404(Director,pk=director_pk)
    if request.method=='POST':
        if director.like_users.filter(pk=request.user.pk).exists():
            director.like_users.remove(request.user)
        else:
            director.like_users.add(request.user)
    serializer=DirectorDetailSerializer(director)
    return Response(serializer.data)


# 전체 장르 요청
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def genre_list(request):
    # actors=Actor.objects.all()
    genres=get_list_or_404(Genre)
    serializer=GenreSerializer(genres,many=True)
    return Response(serializer.data)

# 장르 detail, 좋아요
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def genre_detail(request,genre_pk):
    genre=get_object_or_404(Genre,pk=genre_pk)
    if request.method=='POST':
        print("에러 확인...")
        if genre.like_users.filter(pk=request.user.pk).exists():
            genre.like_users.remove(request.user)
        else:
            genre.like_users.add(request.user)
        serializer=GenreDetailSerializer(genre)
        return Response(serializer.data)
    if request.method=='GET':
        page=int(request.GET.get('page'))
        print(page)
        # movies=Movie.objects.all()[page*100:(page+1)*100]
        serializer=MovieSerializer(genre.movies.all()[page*100:(page+1)*100],many=True)
        return Response(serializer.data)

# 추천 알고리즘
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def recommend(request,genre_pk):
    genre=get_object_or_404(Genre,pk=genre_pk)
    if request.method=='GET':
        current_month = date.today().month
        print(current_month)
        movie=genre.movies.all().filter(release_date__month=current_month)
        cnt=1
        while not movie.exists():
            if cnt>7:
                break
            calc_month=current_month+cnt
            if calc_month>12:
                calc_month-=12
            print(calc_month)
            movie=genre.movies.all().filter(release_date__month=calc_month)
            if movie.exists():
                break

            calc_month=current_month-cnt
            if calc_month<1:
                calc_month+=12
            print(calc_month)   
            movie=genre.movies.all().filter(release_date__month=calc_month)
            if movie.exists():
                break
            cnt+=1
        if movie.exists():
            recommend_movie = random.choice(movie)
            serializer=MovieDetailSerializer(recommend_movie)
            return Response(serializer.data)
        else:
            movie=get_list_or_404(Movie)
            recommend_movie = random.choice(movie)
            serializer=MovieDetailSerializer(recommend_movie)
            return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

# 전체 리뷰 조회
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def review_list(request):
    reviews=Review.objects.all()
    serializer=ReviewSerializer(reviews,many=True)
    return Response(serializer.data)

################################# 수정 중
# path('reviews/<int:review_pk>',views.review_detail),
#
@permission_classes([IsAuthenticated])
#
@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    # 리뷰 조회
    if request.method=='GET':
        serializer=ReviewDetailSerializer(review)
        return Response(serializer.data)
    # 리뷰 수정
    if request.method=='PUT':
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # 리뷰 삭제
    if request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# review create 리뷰생성
@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request,movie_pk):
    movie=get_object_or_404(Movie,id=movie_pk)
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 수정한 내용
        # serializer.save(user=request.user)
        # serializer.save(movie=movie) 를 사용하면 오류가 뜸...
        # 추가로 model에 오타가 난 내용이 pychache에 저장돼 DB가 제대로 생성되지 않아서 수정함.
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# review 좋아요
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def review_like(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    if review.likes.filter(pk=request.user.pk).exists():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)
    serializer=ReviewDetailSerializer(review)
    return Response(serializer.data)





# comment create 댓글생성
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_comment(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    serializer=CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
# 댓글 수정, 삭제
@permission_classes([IsAuthenticated])
@api_view(['PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment=get_object_or_404(Comment,pk=comment_pk)
    # 댓글 수정
    if request.method=='PUT':
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # 댓글 삭제
    if request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# get rating
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_rating(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    rating = Rating.objects.filter(movie=movie, user=request.user).first()
    print(rating)
    if rating:
        print("잘 들어왔다")
        serializer=RatingSerializer(rating)
        print(rating.score)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

# rating create 평점생성
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_rating(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    rating = Rating.objects.filter(movie=movie, user=request.user).first()
    if rating:
        print(rating)
        print(rating.score)
        print(request.data.get('score'))
        print(type(request.data['score']))
        rating.score = request.data.get('score')
        rating.save()
        serializer = RatingSerializer(rating)
    else:
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

# rating 수정, 삭제
@permission_classes([IsAuthenticated])
@api_view(['PUT','DELETE'])
def rating_detail(request,rating_pk):
    rating=get_object_or_404(rating,pk=rating_pk)
    # rating 수정
    if request.method=='PUT':
        serializer=RatingSerializer(rating,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # rating 삭제
    if request.method=='DELETE':
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################################# 수정 중


# @api_view(['POST'])
# def create_review(request,movie_pk):
#     movie=get_object_or_404(Movie,pk=movie_pk)
#     serializer=ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(movie=movie)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


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