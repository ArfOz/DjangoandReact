from django.urls import path
from .views import PostList, CategoryList, CommentList, PostViewList,LikeList

app_name ="blog"

urlpatterns = [
    path("", PostList.as_view(), name="list"),
    path("<category>/", CategoryList.as_view(), name="category-list"),
    # path("<>/", CommentList.as_view(), name="detail"),
    # path("<str:slug>/update/", PostViewList.as_view(), name="update"),
    # # path("<str:slug>/delete/", post_delete, name="delete"),
    # path("<str:slug>/like/", LikeList.as_view(), name="like"),
]