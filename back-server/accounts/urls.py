from django.urls import path
from accounts import views


urlpatterns = [
    # user detail, like_users
    path('<int:user_pk>/',views.user_detail),
    path('my_user/',views.my_user),
    # like users
    # path('<int:user_pk>/follow/',views.follow),
    #

]