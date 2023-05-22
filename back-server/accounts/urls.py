from django.urls import path
from accounts import views


urlpatterns = [
    # user detail, like_users
    path('<int:user_pk>/',views.user_detail),
    # like users
    # path('<int:user_pk>/follow/',views.follow),
    #

]