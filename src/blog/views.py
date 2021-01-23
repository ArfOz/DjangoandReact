from django.shortcuts import render
from rest_framework import generics
from .models import Category, Comment, Post, Like, PostView
from .serializers import CategorySerializer, PostDetailViewSerializer, PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class PostViewList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = PostView.objects.all()
    permission_classes = [IsAuthenticated]

class PostDetailList(generics.ListAPIView):
    serializer_class = PostDetailViewSerializer
    queryset =Post.objects.all()
    permission_classes = [AllowAny]

class PostUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class LikeList(generics.ListAPIView):
    serializer_class =LikeSerializer
    queryset= Like.objects.all()
    permission_classes = [IsAuthenticated]
