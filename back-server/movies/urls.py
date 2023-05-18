from django.urls import path
from movies import views


urlpatterns = [
    # movie whole
    path('movies/',views.movie_list),
    # movie detail
    path('movies/<int:movie_pk>/',views.movie_detail),
    # movie search & one movie not(detail)
    path('movies/search/<str:movie_title>/',views.movie_title_search_detail),
    # actor whole
    path('actors/',views.actor_list),
    # actor detail
    path('actors/<int:actor_pk>/',views.actor_detail),
    
    path('reviews/',views.review_list),
    path('reviews/<int:review_pk>/',views.review_detail),
    path('movies/<int:movie_pk>/reviews/',views.create_review),


    ## 리뷰
    # path('review/', views.review_list),
    # path('review/<int:article_pk>/', views.review_detail),



    # path('articles/<int:article_pk>/comments/', views.comment_create),
]