from django.urls import path
from .views import PostDetailList, CategoryList, CommentList, PostViewList, LikeList, PostDelete, PostUpdate

app_name ="blog"

urlpatterns = [
    path("", PostViewList.as_view(), name="list"),
    path("category/", CategoryList.as_view(), name="category-list"),
    path("<str:slug>/", PostDetailList.as_view(), name="Post"),
    path("<comment>/", CommentList.as_view(), name="detail"),
    path("<str:slug>/update/", PostUpdate.as_view(), name="update"),
    path("<str:slug>/delete/", PostDelete.as_view(), name="delete"),
    # path("<str:slug>/like/", LikeList.as_view(), name="like"),
]