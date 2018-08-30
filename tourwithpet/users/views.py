from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from tourwithpet.notifications import views as notification_view


class ExploreUser(APIView):

    def get(self, request, format=None):
        five_users = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(five_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    def post(self, request, user_id, format=None):
        user = request.user


        try :
            user_to_follow = models.User.objects.get(id = user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.add(user_to_follow)
        user.save()

        notification_view.create_notification(user,user_to_follow,'follow')

        return Response(status=status.HTTP_200_OK)

        
class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):
        user = request.user
        try :
            user_to_follow = models.User.objects.get(id = user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.remove(user_to_follow)
        user.save()

        return Response(status=status.HTTP_200_OK)

        
class UserProfile(APIView):
    def get(self,request,username,format=None):
        print("user profiles")
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)
        return Response(data = serializer.data, status=status.HTTP_200_OK)


class UserFollowers(APIView):
     def get(self, request, username, format=None):
        print("userfollows")
        
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_folllowers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(
            user_folllowers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserFollowing(APIView):
     def get(self, request, username, format=None):
        print("userfollowing")
        
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_following = found_user.following.all()
        serializer = serializers.ListUserSerializer(
            user_following, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class Search(APIView):

    def get(self, request,format=None):

        username = request.query_params.get('username', None)

        if username is not None:
            users = models.User.objects.filter(username__istartswith=username)
            serializer = serializers.ListUserSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            


# from django.contrib.aut
# h import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView

# User = get_user_model()


# class UserDetailView(LoginRequiredMixin, DetailView):

#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"


# user_detail_view = UserDetailView.as_view()


# class UserListView(LoginRequiredMixin, ListView):

#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"


# user_list_view = UserListView.as_view()


# class UserUpdateView(LoginRequiredMixin, UpdateView):

#     model = User
#     fields = ["name"]

#     def get_success_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})

#     def get_object(self):
#         return User.objects.get(username=self.request.user.username)


# user_update_view = UserUpdateView.as_view()


# class UserRedirectView(LoginRequiredMixin, RedirectView):

#     permanent = False

#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})


# user_redirect_view = UserRedirectView.as_view()
