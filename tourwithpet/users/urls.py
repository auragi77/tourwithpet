from django.urls import path
from . import views

app_name ="users"
urlpatterns =[
    # url(




    path("explore/", view=views.ExploreUser.as_view(), name="explorer_user"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnFollowUser.as_view(), name="unFollow_user"),
    path("search/", view=views.Search.as_view(), name="search"),
    path("<str:username>/", view=views.UserProfile.as_view(), name="user_profile"),
    path("<str:username>/followers/", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/following/", view=views.UserFollowing.as_view(), name="user_following"),
    path("<str:username>/password/", view=views.ChangePassword.as_view(), name="change_password"),
    path("login/facebook/", view=views.FacebookLogin.as_view(), name="fb_login"),
    # path("login/google/", view=views.GoogleLogin.as_view(), name="google_login"),
]

