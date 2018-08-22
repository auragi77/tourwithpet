from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        print(user)

        following_users = user.following.all()

        print(following_users)

        image_list =[]

        for following_user in following_users:

            user_images =following_user.images.all()[:2] 

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda x : x.created_at, reverse=True)
        print(sorted_list)

        serializer = serializers.ImageSerializer(sorted_list, many=True)
        return Response(serializer.data)



class LikeImage(APIView):

    def get(self,request,image_id,format=None):

        user = request.user
        print(image_id)

        try:
            found_image = models.Image.objects.get(id=image_id)
            
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )

            new_like.save()

        except models.Image.DoesNotExist:
            return Response(status=404)

        return Response(status=200)







# def get_key(image):
#     return image.created_at
# class ListAllImages(APIView):

#     def get(self,request,format=None):

#         all_images = models.Image.objects.all()

#         serializer = serializers.ImageSerializer(all_images, many=True)

#         return Response(data=serializer.data)
        

# class ListAllComments(APIView):

#     def get(self,request, fromat=None):

#         all_comments = models.Comment.objects.all()

#         serializer = serializers.CommentSerializer(all_comments, many=True)

#         return Response(data=serializer.data)




# class ListAllLikes(APIView):

#     def get(self,request, fromat=None):

#         all_likes = models.Like.objects.all()

#         serializer = serializers.LikeSerializer(all_likes, many=True)

#         return Response(data=serializer.data)