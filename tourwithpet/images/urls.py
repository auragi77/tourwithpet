from django.urls import path
from . import views

app_name ="images"
urlpatterns =[
    # url(
    #     regex=r'all/$',
    #     view=views.ListAllImages.as_view(),
    #     name='all_images'
    # )
    path("all/", view=views.ListAllImages.as_view(), name="all_images"),
]