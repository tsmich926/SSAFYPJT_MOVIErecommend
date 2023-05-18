from rest_framework import serializers
from .models import Movie,Actor,Director,Genre,Review,Ratings,Comment
from django.conf import settings
from accounts.serializers import UserSerializer

# 주의사항
# 참조키가 모델에 있는 경우 readonly로 바꾼 다음 serializer.save('title'=title)와 같이 사용해야 함
# manytomanyfiled는 


# base

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=('movie',)

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ratings
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'



# movies/
# 영화 전체 목록
# movies/search/<str:movie_title>/
# 영화 검색 시 보내줄 데이터
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'



# movies/<int:movie_pk>/
# 영화 디테일
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)
    actors=ActorSerializer(many=True,read_only=True)
    directors=DirectorSerializer(many=True,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    review_count=serializers.IntegerField(source='reviews.count',read_only=True)

# actors/<int:actor_pk>/
# 배우 디테일
class ActorDetailSerializer(serializers.ModelSerializer):
    movies=MovieSerializer(many=True,read_only=True)
    like_users=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Actor
        fields='__all__'


#### 여기까지 완료









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




## movies/search/<str:movie_title>/
## 영화 검색 시 보내줄 데이터
class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)